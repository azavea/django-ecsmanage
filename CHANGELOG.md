# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2019-07-15
### Changed
- Use argparse.REMAINDER nargs value [#12](https://github.com/azavea/django-ecsmanage/pull/12)
- Updated Django requirement from <=2.1,>=1.11 to >=1.11,<2.3 [#11](https://github.com/azavea/django-ecsmanage/pull/11)

## [1.0.1] - 2019-05-21
### Added
- Added test suite for matrix of Python/Django versions [#7](https://github.com/azavea/django-ecsmanage/pull/7)

### Fixed
- Fixed support for `future-fstrings` in Python 3.6+ [#9](https://github.com/azavea/django-ecsmanage/pull/9)

## [1.0.0] - 2019-05-01
### Added
- Added Python 2.7 support [#6](https://github.com/azavea/django-ecsmanage/pull/6)

### Fixed
- Fixed reference to taskDefinition in describe_task_definition response [#5](https://github.com/azavea/django-ecsmanage/pull/5)

## [0.1.0] - 2019-04-10
### Added
- Update PyPi credentials [#4](https://github.com/azavea/django-ecsmanage/pull/4)
- Initialize Django module for one-off management commands [#2](https://github.com/azavea/django-ecsmanage/pull/2)

[unreleased]: https://github.com/:azavea/django-ecsmanage/compare/1.1.0...HEAD
[1.1.0]: https://github.com/:azavea/django-ecsmanage/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/:azavea/django-ecsmanage/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/azavea/django-ecsmanage/compare/0.1.0...1.0.0
[0.1.0]: https://github.com/azavea/django-ecsmanage/releases/tag/0.1.0
