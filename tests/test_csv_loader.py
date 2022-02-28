import pytest

# from io import StringIO
import csv
from unittest.mock import mock_open, patch, MagicMock

from table_analyser.csv_loader import CSVLoader


TEST_CSV_DATA = """Col 1,Col 2\none,two"""

def test_create_csv_reader_from_file_data():
    """It returns csv.reader iterable with csv data."""
    mocked_open = mock_open(read_data=TEST_CSV_DATA)
    with patch('builtins.open', mocked_open):
        reader = CSVLoader('test/file/path.csv').load_csv()
    reader_content = list(reader)
    assert reader_content[0] == ["Col 1", "Col 2"]
    assert reader_content[1] == ["one", "two"]


def test_load_data_from_reader_to_instance_variables():
    """It adds headers and rows when constructor runs."""
    mocked_open = mock_open(read_data=TEST_CSV_DATA)
    with patch('builtins.open', mocked_open):
        loader = CSVLoader('test/file/path.csv')
    assert loader.headers ==  ["Col 1", "Col 2"]
    assert loader.rows == [["one", "two"]]


def test_returns_headers_and_rows_as_object():
    """It returns single object with headers and row data."""
    mocked_open = mock_open(read_data=TEST_CSV_DATA)
    with patch('builtins.open', mocked_open):
        loader = CSVLoader('test/file/path.csv')
    assert loader.data() == {
        "headers": ["Col 1", "Col 2"], 
        "rows": [["one", "two"]]
    }