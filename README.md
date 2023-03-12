# apple-news-to-sqlite

Export Apple News Saved Stories to SQLite

## Install

    pip install apple-news-to-sqlite

## Source Code

[apple-news-to-sqlite](https://github.com/RhetTbull/apple-news-to-sqlite)

## Usage

    apple-news-to-sqlite articles.db
    
    apple-news-to-sqlite --dump

## CLI Help

<!-- [[[cog
import cog
from apple_news_to_sqlite.cli import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli, ["--help"])
help = result.output.replace("Usage: cli", "Usage: apple-news-to-sqlite")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```
Usage: apple-news-to-sqlite [OPTIONS] [DB_PATH]

  Export your Apple News saved stories/articles to a SQLite database

  Example usage:

      apple_news_to_sqlite articles.db

  This will populate articles.db with an "articles" table containing information
  about your saved articles.

  Note: the contents of the articles themselves are not stored in the database,
  only metadata about the article such as title, author, url, etc.

Options:
  --version  Show the version and exit.
  --dump     Output saved stories to standard output
  --schema   Create database schema and exit
  --help     Show this message and exit.

```
<!-- [[[end]]] -->

## Using apple-news-to-sqlite in your own Python code

`get_saved_articles()` returns a list of dictionaries, each representing a saved article with the
following keys (all strings):

    * id
    * url
    * title
    * description
    * image
    * author

```pycon
>>> from apple_news_to_sqlite import get_saved_articles
>>> articles = get_saved_articles()
```

## Contributing

Contributions of all types are welcome! Fork the repo, make a branch, and submit a PR.

See [README_DEV.md](README_DEV.md) for developer notes.

## Thanks

Thanks to [Simon Willison](https://simonwillison.net/) who inspired this project
with his excellent "everything-to-sqlite" [dogsheep](https://github.com/dogsheep) project.

Thanks Simon also for the excellent tools
[sqlite-utils](https://github.com/simonw/sqlite-utils) and [Datasette](https://datasette.io).

Thanks also to [Dave Bullock](https://github.com/eecue) who inspired this project and helped
tremendously with the reverse engineering and initial code.

## License

MIT License
