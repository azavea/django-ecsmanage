# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2020-10-13
### Added
- Add support for Django 3.x and Python 3.8; no actual code changes were required [#14](https://github.com/azavea/django-ecsmanage/pull/14)
- Add support for Django 3.1 and Black source code formatting [#25](https://github.com/azavea/django-ecsmanage/pull/25)
- Add support for supplying Fargate platform version [#26](https://github.com/azavea/django-ecsmanage/pull/26)
- Add support for overriding Django container name [#27](https://github.com/azavea/django-ecsmanage/pull/27)

### Removed
- Remove support for end-of-life Python 2.7 and 3.4 [#16](https://github.com/azavea/django-ecsmanage/pull/16)
- Remove support for end-of-life Python 3.5 [#25](https://github.com/azavea/django-ecsmanage/pull/25)
- Remove support for end-of-life Django 2.0 and 2.1 [#16](https://github.com/azavea/django-ecsmanage/pull/16)
- Remove support for end-of-life Django 1.11 [#22](https://github.com/azavea/django-ecsmanage/pull/22)

### Changed
- Updated `tox` and Travis configs to improve efficiencies, remove deprecated settings, and implement current best practices [#16](https://github.com/azavea/django-ecsmanage/pull/16)
- Moved most package distribution configuration from setup.py to setup.cfg [#16](https://github.com/azavea/django-ecsmanage/pull/16)
- Migrate from Travis to GitHub Actions [#22](https://github.com/azavea/django-ecsmanage/pull/22)

### Fixed
- Fixed `flake8` config in scripts/test to ignore eggs [#16](https://github.com/azavea/django-ecsmanage/pull/16)
- Fixed `black` formatter path in scripts/test to check all Python files [#16](https://github.com/azavea/django-ecsmanage/pull/16)

## [1.1.0] - 2019-07-15
### Changed
- Use argparse.REMAINDER nargs value [#12](https://github.com/azavea/django-ecsmanage/pull/12)
- Updated Django requirement from &lt;=2.1,>=1.11 to >=1.11,&lt;2.3 [#11](https://github.com/azavea/django-ecsmanage/pull/11)

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

[Unreleased]: https://github.com/azavea/django-ecsmanage/compare/2.0.0...HEAD
[2.0.0]: https://github.com/azavea/django-ecsmanage/compare/1.1.0...2.0.0
[1.1.0]: https://github.com/:azavea/django-ecsmanage/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/:azavea/django-ecsmanage/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/azavea/django-ecsmanage/compare/0.1.0...1.0.0
[0.1.0]: https://github.com/azavea/django-ecsmanage/releases/tag/0.1.0
