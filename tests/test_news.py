"""Test the news.py module for reading saved articles from Apple News"""

import os

from apple_news_to_sqlite.news import get_saved_articles

skip_ids = ["AdFMWrpVxQk2Qp0AP_Is3OA"]


def test_get_saved_articles():
    """Test the get_saved_articles function"""
    reading_list = os.path.join(os.getcwd(), "tests", "data", "reading-list")
    articles = get_saved_articles(reading_list)

    assert len(articles) == 2


def test_get_saved_articles_with_skip():
    """Test the get_saved_articles function with a skip list"""
    reading_list = os.path.join(os.getcwd(), "tests", "data", "reading-list")
    articles = get_saved_articles(reading_list, skip_article_ids=skip_ids)

    assert len(articles) == 1
