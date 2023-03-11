"""CLI for apple_news_to_sqlite"""

import click
import sqlite_utils
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
def main(db_path, dump, schema):
    """Export your Apple News saved stories/articles to a SQLite database

    Example usage:

        apple_news_to_sqlite articles.db

    This will populate articles.db with an "articles" table containing information about
    your saved articles.

    Note: the contents of the articles themselves are not stored in the database, only
    metadata about the article such as title, author, url, etc.
    """
    pass