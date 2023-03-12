"""CLI for apple_news_to_sqlite"""

from __future__ import annotations

import sys

import click
import sqlite_utils
from rich import print

from .news import get_saved_articles
from .version import __version__


@click.command()
@click.version_option(version=__version__)
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=False,
)
@click.option("--dump", is_flag=True, help="Output saved stories to standard output")
@click.option("--schema", is_flag=True, help="Create database schema and exit")
def cli(db_path, dump, schema):
    """Export your Apple News saved stories/articles to a SQLite database

    Example usage:

        apple_news_to_sqlite articles.db

    This will populate articles.db with an "articles" table containing information about
    your saved articles.

    Note: the contents of the articles themselves are not stored in the database, only
    metadata about the article such as title, author, url, etc.
    """
    if not db_path and not dump:
        raise click.UsageError(
            "Please specify a path to a database file, or use --dump to see the output",
        )

    if dump:
        articles = get_saved_articles()
        for article in articles:
            print(article)
        sys.exit(0)

    db = sqlite_utils.Database(db_path)
    create_schema(db)
    if schema:
        # Our work is done
        return

    articles = get_saved_articles()
    for article in articles:
        db["articles"].upsert(article, pk="id", alter=True)

    print(
        f"Saved {len(articles)} {'articles' if len(articles) != 1 else 'article'} to {db_path}"
    )


def create_schema(db: sqlite_utils.Database) -> None:
    """Create the database schema"""
    if not db["articles"].exists():
        db["articles"].create(
            {
                "id": str,
                "date": str,
                "url": str,
                "title": str,
                "description": str,
                "image": str,
                "author": str,
            },
            pk="id",
        )
