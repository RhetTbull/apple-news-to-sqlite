# Developer Notes

This project uses poetry for dependency management and packaging.

* `pip install poetry`
* `poetry install`
* `poetry run python -m apple_news_to_sqlite --help`

[bump2version](https://github.com/c4urself/bump2version) is used for bumping the version.

`bump2version` is installed as a dev dependency, so you can run it like this:

* `poetry run bump2version minor --verbose --dry-run`

Run again without `--dry-run` to actually bump the version.

[doit](https://pydoit.org/) is used for running tasks:

* `poetry run doit list`

[cogapp](https://nedbatchelder.com/code/cog) is used for updating the README.md (called via `doit`)

## Testing

* `poetry run pytest`