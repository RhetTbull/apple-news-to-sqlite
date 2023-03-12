# Changelog for apple-news-to-sqlite

All notable changes to this project will be documented in this file.

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
