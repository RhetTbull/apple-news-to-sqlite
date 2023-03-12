# Changelog for apple-news-to-sqlite

All notable changes to this project will be documented in this file.

## Initial Release

[v0.3.0](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.3.0)

### 11 March 2023

### New

- Working version!

    apple-news-to-sqlite articles.db

    apple-news-to-sqlite --dump

### Contributors

- @RhetTbull for initial release
- @eecue for help with the reverse engineering and initial code

### Thanks

Special thanks to @simonw for inspring this with his @dogsheep projects!

## Added date to article dict and database

[v0.2.0](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.2.0)

### 11 March 2023

### Added

Added `date: datetime.datetime` to article dict returned by `get_saved_articles()`

### Contributors

- @RhetTbull for code
