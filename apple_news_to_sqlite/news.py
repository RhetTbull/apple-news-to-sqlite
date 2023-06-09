"""
Utilities for reading Apple News data

Get your "Saved Stories" articles from Apple News

Thanks to Dave Bullock (https://github.com/eecue) who's idea this was and who wrote the extract_info_from_apple_news function
"""


from __future__ import annotations

import contextlib
import io
import pathlib
import plistlib

import requests
from bs4 import BeautifulSoup

__all__ = ["get_saved_articles"]


def get_reading_list_bplist(reading_list_file: str | None = None) -> bytes | None:
    """Get saved articles info from Apple News

    Returns:
        bytes: The saved articles binary plist as a bytes object
        None: If the saved articles are not found
    """
    # The saved articles are stored in a binary file called reading-list
    # in the Apple News container (~/Library/Containers/com.apple.news)
    # The file contains at least two binary plist (bplist) files
    # embedded in it, the second of which contains the saved article IDs
    # (The first is a binary NSKeyedArchiver archive)
    # This function finds the second bplist file and returns it as a bytes object
    # or None if the file is not found

    news_container = (
        "~/Library/Containers/com.apple.news/"
        + "Data/Library/Application Support/com.apple.news/"
        + "com.apple.news.public-com.apple.news.private-production"
    )
    reading_list_file = reading_list_file or (
        pathlib.Path(news_container, "reading-list").expanduser().absolute()
    )
    bplist_marker = b"\x62\x70\x6C\x69\x73\x74\x30\x30"  # bplist00

    reading_list = open(reading_list_file, "rb")
    length = reading_list.seek(0, io.SEEK_END)
    reading_list.seek(io.SEEK_SET)
    found = 0
    while window := reading_list.peek(1):
        if len(window) >= 8 and window[:8] == bplist_marker:
            found += 1
            if found == 2:
                return reading_list.read(length - reading_list.tell())
        reading_list.read(1)
    return None


def get_article_info(reading_list: bytes) -> dict[str, dict[str, str]] | None:
    """Decode the saved article information from the binary plist"""
    return plistlib.loads(reading_list, fmt=plistlib.FMT_BINARY)


def extract_info_from_apple_news(news_id: str) -> dict[str, str]:
    """Extract the article URL, title, description, image, and author from Apple News"""

    # Construct the Apple News URL from the ID
    apple_news_url = f"https://apple.news/{news_id}"

    # Send a GET request to the Apple News URL and get the response HTML
    response = requests.get(apple_news_url)
    html = response.content.decode("utf-8")

    # Use BeautifulSoup to extract the URL from the redirectToUrlAfterTimeout function
    soup = BeautifulSoup(html, "html.parser")
    if script_tag := soup.find(
        "script", string=lambda t: "redirectToUrlAfterTimeout" in t
    ):
        try:
            url_start_index = script_tag.text.index('"https://') + 1
            url_end_index = script_tag.text.index('"', url_start_index)
            url = script_tag.text[url_start_index:url_end_index]
        except ValueError:
            # Some articles are only available in the Apple News app and don't have a URL
            url = None
    else:
        url = None

    if url is None:
        # try to get the URL from the apple-itunes-app meta tag
        # meta tag looks like this:
        # <meta name="apple-itunes-app" content="app-id=1066498020, app-argument=https://apple.news/AfQfio2vcSIifL0FrjGynZA" />
        if app_link := soup.find("meta", {"name": "apple-itunes-app"}):
            app_link_tags = dict(
                [tag.strip().split("=") for tag in app_link["content"].split(",")]
            )
            with contextlib.suppress(KeyError):
                url = app_link_tags["app-argument"]

    # Extract the og:title, og:description, og:image, and author meta tags
    if title_tag := soup.find("meta", property="og:title"):
        title = title_tag["content"]
    else:
        title = None

    if description_tag := soup.find("meta", property="og:description"):
        description = description_tag["content"]
    else:
        description = None

    if image_tag := soup.find("meta", property="og:image"):
        image = image_tag["content"]
    else:
        image = None

    if author_tag := soup.find("meta", {"name": "Author"}):
        author = author_tag["content"]
    else:
        author = None

    # Return the extracted information as a dictionary
    return {
        "id": news_id,
        "url": url,
        "title": title,
        "description": description,
        "image": image,
        "author": author,
    }


def get_saved_articles(
    reading_list_file: str | None = None, skip_article_ids: list[str] | None = None
) -> list[dict[str, str]]:
    """Get saved articles from Apple News

    Args:
        reading_list_file (str, optional): The path to the reading-list file. Defaults to None.
        skip_article_ids (list[str], optional): A list of article IDs to skip. Defaults to None.

    Returns:
        list: a list of saved article dictionaries

    Notes:
        If reading_list_file is not specified, the default location is used.
        This is probably what you want.

        If you want to skip downloading information for certain articles, for example, previously
        downloaded articles, you can specify a list of article IDs to skip.

        The return dictionaries contain the following keys:
            id: str; the article ID
            url: str; the article URL
            title: str; the article title
            description: str; the article description
            image: str; the article image URL
            author: str; the article author
            date: datetime.datetime; the date the article was saved (in GMT)
    """
    skip_article_ids = skip_article_ids or []

    # Get the saved articles binary plist
    reading_list = get_reading_list_bplist(reading_list_file=reading_list_file)

    # Decode the saved articles binary plist
    article_info = get_article_info(reading_list)

    # Extract the article information from Apple News
    saved_articles = []
    for article in article_info.values():
        article_id = article["articleID"]
        if article_id in skip_article_ids:
            continue
        info = extract_info_from_apple_news(news_id=article_id)
        info["date"] = article_info[f"rl-{info['id']}"]["dateAdded"]
        saved_articles.append(info)

    return saved_articles
