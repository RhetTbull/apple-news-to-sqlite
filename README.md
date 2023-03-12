# apple-news-to-sqlite

Export Apple News Saved Stories to SQLite

## Install

    pip install apple-news-to-sqlite

## Source code

[apple-news-to-sqlite](https://github.com/RhetTbull/apple-news-to-sqlite)

## Usage

    apple-news-to-sqlite articles.db
    
    apple-news-to-sqlite --dump

Your Terminal app will require full disk access in order to access the saved article database in the Apple News app sandbox.

## CLI help

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
following keys:

    * id: str
    * date: datetime.datetime
    * url: str
    * title: str
    * description: str
    * image: str
    * author: str

```pycon
>>> from apple_news_to_sqlite import get_saved_articles
>>> articles = get_saved_articles()
```

## How it works

Through reverse engineering, it was determined that the Apple News app stores
saved articles in a file called `reading-list` in the following directory:

`~/Library/Containers/com.apple.news/Data/Library/Application Support/com.apple.news/com.apple.news.public-com.apple.news.private-production/`

This format of this file is unknown but it is a binary file that contains two embedded 
[binary plist](https://medium.com/@karaiskc/understanding-apples-binary-property-list-format-281e6da00dbd)
files. The first contains an [NSKeyedArchiver](https://developer.apple.com/documentation/foundation/nskeyedarchiver)
object which I have not yet inspected. The second bplist contains a list of saved article IDs along with the date
they were saved. The article IDs are used to look up the article data on Apple's News site and the article data
is extracted with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

## Testing

The code is at the "it works on my machine" stage of testing. (M1 Mini, macOS Ventura 13.1)

If it doesn't work for you, please open a PR!

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
