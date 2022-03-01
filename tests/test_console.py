import os

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


@pytest.fixture(scope="session")
def test_csv_file():
    """It returns an empty TextIO file with csv extension."""
    with open("test.csv", "w") as f:
        yield f
    os.remove("test.csv")


@pytest.mark.e2e
def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_calls_csvloader_with_specified_path(
    runner,
    mock_csvloader,
    test_csv_file,
    # mock_table,
    # mock_queryhelper,
) -> None:
    """It passes file path to csv loader instance."""
    result = runner.invoke(console.main, ["--file-path=test.csv"])
    print(result.__dict__)
    assert result.exit_code == 0
    mock_csvloader.assert_called_with("test.csv")
