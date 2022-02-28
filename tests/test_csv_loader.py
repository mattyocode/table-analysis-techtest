from unittest.mock import mock_open, patch

import pytest

from table_query.csv_loader import CSVLoader

TEST_CSV_DATA = """Col 1,Col 2\none,two"""


def test_load_data_to_instance_variables():
    """It adds headers and rows when constructor runs."""
    mocked_open = mock_open(read_data=TEST_CSV_DATA)
    with patch("builtins.open", mocked_open):
        loader = CSVLoader("test/file/path.csv")
    assert loader.headers == ["Col 1", "Col 2"]
    assert loader.rows == [["one", "two"]]


def test_returns_headers_and_rows_as_object():
    """It returns single object with headers and row data."""
    mocked_open = mock_open(read_data=TEST_CSV_DATA)
    with patch("builtins.open", mocked_open):
        loader = CSVLoader("test/file/path.csv")
    assert loader.data() == {"headers": ["Col 1", "Col 2"], "rows": [["one", "two"]]}


@pytest.mark.e2e
def test_loads_real_file():
    """It loads test file from fixtures dir.
    Uses real file. Is skipped for CI/CD."""
    loader = CSVLoader("fixtures/Python Developer Test Dataset.csv")
    assert "headers" in loader.data()
    assert "rows" in loader.data()


@pytest.mark.e2e
def test_raises_error_when_file_cannot_be_found():
    """It raises .... error when file cannot be found.
    Uses real file. Is skipped for CI/CD."""
    with pytest.raises(FileNotFoundError):
        loader = CSVLoader("fixtures/fake-filename.csv")
