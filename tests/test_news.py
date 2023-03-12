"""Test the news.py module for reading saved articles from Apple News"""

import os

from apple_news_to_sqlite.news import get_saved_articles


def test_get_saved_articles():
    """Test the get_saved_articles function"""
    reading_list = os.path.join(os.getcwd(), "tests", "data", "reading-list")
    articles = get_saved_articles(reading_list)

    assert len(articles) == 2
