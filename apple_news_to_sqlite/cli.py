"""CLI for apple_news_to_sqlite"""

from __future__ import annotations

import datetime
import json
import sys

import click
import sqlite_utils
from rich import print

from .news import get_saved_articles
from .version import __version__


@click.command()
@click.version_option(version=__version__)
@click.option(
    "--dump",
    "--json",
    is_flag=True,
    help="Print saved stories to standard output as JSON.",
)
@click.option(
    "--all",
    "all_articles",
    is_flag=True,
    help="Process all saved articles; "
    "if not specified, only saved articles that have not previously been stored in the database"
    "are processed.",
)
@click.option("--schema", is_flag=True, help="Create database schema and exit.")
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=False,
)
def cli(dump, all_articles, schema, db_path):
    """Export your Apple News saved stories/articles to a SQLite database

    Example usage:

        apple-news-to-sqlite articles.db

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
        dump_articles(articles)
        sys.exit(0)

    db = sqlite_utils.Database(db_path)
    create_schema(db)

    if schema:
        # Our work is done
        return

    if all_articles:
        skip_article_ids = []
    else:
        skip_article_ids = [row["id"] for row in db["articles"].rows_where()]
        print(
            f"Skipping {len(skip_article_ids)} previously saved {'article' if len(skip_article_ids) == 1 else 'articles'}."
        )
    articles = get_saved_articles(skip_article_ids=skip_article_ids)
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


def dump_articles(articles: list[dict[str, str]]) -> None:
    """Dump articles to standard output"""

    def default(obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError

    print(json.dumps(articles, indent=2, default=default))
