"""Test the apple-news-to-sqlite CLI"""

import pathlib

import pytest
from click.testing import CliRunner

from apple_news_to_sqlite.cli import cli


@pytest.mark.parametrize("arg", ["--dump", "--json"])
def test_cli_dump(arg):
    """Test the CLI with --dump"""
    runner = CliRunner()
    result = runner.invoke(cli, [arg])
    assert result.exit_code == 0
    assert result.output.startswith("[")
    assert result.output.strip().endswith("]")


def test_cli_schema():
    """Test the CLI with --schema"""
    with CliRunner().isolated_filesystem():
        result = CliRunner().invoke(cli, ["--schema", "articles.db"])
        assert result.exit_code == 0
        assert pathlib.Path("articles.db").exists()


def test_cli_save_articles():
    """Test the CLI with a database path"""
    with CliRunner().isolated_filesystem():
        result = CliRunner().invoke(cli, ["articles.db"])
        assert result.exit_code == 0
        assert pathlib.Path("articles.db").exists()
