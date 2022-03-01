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

## Notes

This was really fun to do, and I hope my solution is clear and as expected.

My main focus has been to create a reusable Table class that can manipulate and return tabular data (given that Pandas and data analysis libraries shouldn't be used). More complex operations on table data are undertaken by the QueryHelper class, which is directed at satisfying the output requirements of the task.

I've included list comprehension in the `__str__` method, and two filtering methods of the Table class. The filtering methods are therefore not optimised but they could be refactored to use sorted input and binary search if optimisation was needed.

Test coverage is at 100%, although there are certainly some edge cases that aren't covered. There are also occasions where methods expect a certain type and currently the happy path is assumed – these could be caught with type checking and error raising, but I've assumed (hopefully correctly) that's beyond the scope of this task.

In some instances, I wasn't entirely sure on the required output - specifically whether things like 'list of 5 items' referred to a whole row, or the individual value itself. Hoping to make the data as clear as possible, I've returned results in tabular format with headers, and excluded certain columns for the outputs where full data wasn't specified, mostly to make sure the output is legible in the terminal on narrower screens.

Thanks!

:grin:
