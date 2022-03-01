# Python Developer Tech Test

[![Tests](https://github.com/mattyocode/table-analysis-techtest/workflows/Tests/badge.svg)](https://github.com/mattyocode/table-analysis-techtest/actions?workflow=Tests)

[![codecov](https://codecov.io/gh/mattyocode/table-analysis-techtest/branch/main/graph/badge.svg?token=VM1SWZJRFW)](https://codecov.io/gh/mattyocode/table-analysis-techtest)

## Requirements

- Python ^3.9
- Poetry ^1.1

## How to install

1. Clone from Github

   ```bash
   cd projects
   git clone <repo-tag>
   ```

2. Install dependencies

   Make sure [Poetry is installed](https://python-poetry.org/docs/) and run `poetry install` to install project dependencies.

3. Run tests with Pytest

   ```bash
   poetry run pytest --cov
   ```

4. Run linting with Flake8

   ```bash
   poetry run flake8 .
   ```

## How to run table queries

- Once Poetry has installed dependencies, run

  ```bash
  poetry run table-query
  ```

  to run all four of the required reports.

- To run function that returns the 'first 5 items from the resultant list and output to the console', add `--smallest-values` flag, e.g.

  ```bash
  poetry run table-query --smallest-values
  ```

- To run function that returns the 'new list of mast data with “Lease Years” = 25 years' and 'total rent', add `--lease-years-equal` flag, e.g.

  ```bash
  poetry run table-query --lease-years-equal
  ```

- To run function that returns 'a dictionary containing tenant name and a count of masts for each tenant', add `--tenant-mast-count` flag, e.g.

  ```bash
  poetry run table-query --tenant-mast-count
  ```

- To run function that returns 'a dictionary containing tenant name and a count of masts for each tenant', add `--start-date-range` flag, e.g.

  ```bash
  poetry run table-query --start-date-range
  ```

- A `--file-path` flag can also be passed in, although is not necessary as the default is set to 'fixtures/Python Developer Test Dataset.csv' where the test data provided is located.

## Example output

When running `poetry run table-query` (i.e. without any flags), the output is as follows:

![Terminal output screengrab](https://github.com/mattyocode/images/blob/main/table-analysis-techtest/table-analysis-output-e.png)
