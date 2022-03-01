import os
from unittest.mock import call

import click.testing

import pytest

from table_query import console


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_table(mocker):
    """Fixture for mocking Table."""
    return mocker.patch("table_query.console.Table")


@pytest.fixture
def mock_csvloader(mocker):
    """Fixture for mocking CSVLoader."""
    return mocker.patch("table_query.console.CSVLoader")


@pytest.fixture
def mock_queryhelper(mocker):
    """Fixture for mocking QueryHelper."""
    return mocker.patch("table_query.console.QueryHelper")


@pytest.fixture
def test_csv_file():
    """It returns an empty TextIO file with csv extension."""
    with open("test.csv", "w") as f:
        yield f
    os.remove("test.csv")


@pytest.mark.e2e
def test_main_succeeds(runner):
    """It exits with status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_calls_csvloader_with_specified_path(
    runner,
    mock_csvloader,
    test_csv_file,
    mock_table,
) -> None:
    """It passes file path to csv loader instance."""
    result = runner.invoke(console.main, ["--file-path=test.csv"])
    assert result.exit_code == 0
    mock_csvloader.assert_called_with("test.csv")
    mock_table.assert_called()


def test_main_calls_smallest_by_value_when_flag_passed(
    runner,
    test_csv_file,
    mock_queryhelper,
) -> None:
    """It passes default args to QueryHelper instance."""
    result = runner.invoke(console.main, ["--file-path=test.csv", "--smallest-values"])
    assert result.exit_code == 0
    instance = mock_queryhelper.return_value
    assert instance.smallest.call_args == call(5, "Current Rent")
    assert "Smallest 5 values of Current Rent in ascending order" in result.output


def test_main_calls_masts_data_equals_when_flag_passed(
    runner,
    test_csv_file,
    mock_table,
) -> None:
    """It passes default args to Table instance.."""
    result = runner.invoke(
        console.main, ["--file-path=test.csv", "--lease-years-equal"]
    )
    assert result.exit_code == 0
    instance = mock_table.return_value
    assert instance.get_rows_equal_to.call_args == call("Lease Years", "25")
    assert "Mast data where Lease Years is equal to 25" in result.output


def test_main_calls_tenant_mast_count_when_flag_passed(
    runner,
    test_csv_file,
    mock_queryhelper,
) -> None:
    """It passes default args to QueryHelper instance."""
    result = runner.invoke(
        console.main, ["--file-path=test.csv", "--tenant-mast-count"]
    )
    assert result.exit_code == 0
    instance = mock_queryhelper.return_value
    assert instance.frequency.call_args == call("Tenant Name")
    assert "Count of masts by tenant" in result.output


def test_prints_dict_when_it_has_values(
    runner,
    test_csv_file,
    mock_queryhelper,
) -> None:
    """It prints frequency dict to console."""
    mock_queryhelper.return_value.frequency.return_value = {"Tenant": 3}
    result = runner.invoke(
        console.main, ["--file-path=test.csv", "--tenant-mast-count"]
    )
    assert result.exit_code == 0
    assert "Tenant: 3 masts" in result.output


def test_main_calls_mast_data_in_date_range_when_flag_passed(
    runner,
    test_csv_file,
    mock_queryhelper,
) -> None:
    """It passes default args to QueryHelper instance."""
    result = runner.invoke(console.main, ["--file-path=test.csv", "--start-date-range"])
    assert result.exit_code == 0
    instance = mock_queryhelper.return_value
    assert instance.dates_between.call_args == call(
        "01 Jun 1999", "31 Aug 2007", "Lease Start Date"
    )
    assert (
        "Mast data where Lease Start Date is between 01 Jun 1999 and 31 Aug 2007"
        in result.output
    )


def test_main_calls_all_functions_when_no_flag_passed(
    runner,
    test_csv_file,
    mock_table,
    mock_queryhelper,
) -> None:
    """It passes default args to QueryHelper instance."""
    result = runner.invoke(console.main, ["--file-path=test.csv"])
    assert result.exit_code == 0
    assert "Smallest 5 values of Current Rent in ascending order" in result.output
    assert "Mast data where Lease Years is equal to 25" in result.output
    assert "Count of masts by tenant" in result.output
    assert (
        "Mast data where Lease Start Date is between 01 Jun 1999 and 31 Aug 2007"
        in result.output
    )
