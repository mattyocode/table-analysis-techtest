# Python Developer Tech Test

[![Tests](https://github.com/mattyocode/table-analysis-techtest/workflows/Tests/badge.svg)](https://github.com/mattyocode/table-analysis-techtest/actions?workflow=Tests)

[![codecov](https://codecov.io/gh/mattyocode/table-analysis-techtest/branch/main/graph/badge.svg?token=VM1SWZJRFW)](https://codecov.io/gh/mattyocode/table-analysis-techtest)

## Requirements

- Python ^3.9
- Poetry ^1.1

## Install dependencies with Poetry

To install Poetry itself see Poetry [documentation](https://python-poetry.org/docs/).

Then run `poetry install` to install dependencies.

## Run tests with Poetry

`$ poetry run pytest --cov`

## Run linting with Poetry

`$ poetry run flake8 .`

`$ poetry run black .`
