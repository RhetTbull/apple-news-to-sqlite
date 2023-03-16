# Changelog for apple-news-to-sqlite

All notable changes to this project will be documented in this file.

## Bug Fix

[v0.5.2](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.5.2)

### 15 March 2023

### Changed

- Removed concurrent downloads to avoid time out errors on Apple's news website

### Contributors

- @RhetTbull for code changes

## Threaded downloads

[v0.5.1](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.5.1)

### 12 March 2023

### Changed

- Threaded downloads: To get the article metadata, apple-news-to-sqlite must download data from https://apple.news for each saved article.
This version uses concurrent.futures to allow multiple threads to do the download in parallel, which is much faster
for large reading lists.

### Contributors

- @RhetTbull for code changes

## Fixed PyPI metadata

[v0.4.2](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.4.2)

### 12 March 2023

### Changed

- Added homepage and keywords to PyPI metadata

### Contributors

- @RhetTbull

## Fixed typo in help

[v0.4.1](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.4.1)

### 12 March 2023

### Changed

- Fixed typo in help

### Contributors

- @RhetTbull

## Add JSON output, skipping of previously saved articles

[v0.4.0](https://github.com/RhetTbull/apple-news-to-sqlite/releases/tag/v0.4.0)

### 12 March 2023

### Changed

- --dump now dumps articles as JSON
- Only articles not previously saved are processed, added --all to save all articles

### Contributors

- @RhetTbull for code

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
