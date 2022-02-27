from cgi import test
import pytest

from table_analyser.table import Table


def test_initalise_table_with_test_data():
    test_headers = ["Col 1"]
    test_row = [["a"]]
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row


def test_initalise_table_with_multi_column_test_data():
    test_headers = ["Col 1", "Col 2"]
    test_row = [["a", "b"]]
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row


def test_initalise_table_with_multi_column_multi_row_test_data():
    test_headers = ["Col 1", "Col 2"]
    test_rows = [["a", "b"], ["z", "y"]]
    table = Table(test_headers, test_rows)
    assert table.headers == test_headers
    assert table.rows == test_rows
    assert len(table.headers) == 2
    assert len(table.rows) == 2


def test_initialise_table_with_empty_input_arrays():
    test_headers = []
    test_row = []
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row


def test_table_prints_to_console_evenly_spaced_single_column_long_header():
    long_header = "Col 1"
    test_header = [long_header]
    test_row = [["a"]]
    table = Table(test_header, test_row)
    assert str(table) == "Col 1\n-----\na    "
    for line in str(table).split("\n"):
        assert len(line) == len(long_header)


def test_table_prints_to_console_evenly_spaced_multi_column_long_header():
    long_header = "Col Two"
    test_headers = ["Col 1", long_header]
    test_row = [["a", "bb"]]
    table = Table(test_headers, test_row)
    assert str(table) == "Col 1  |Col Two\n---------------\na      |bb     "
    for line in str(table).split("\n"):
        assert len(line) == len(long_header) * 2 + 1


def test_table_prints_to_console_evenly_spaced_single_column_long_row():
    long_row = "long row value"
    test_header = ["Col 1"]
    test_row = [[long_row]]
    table = Table(test_header, test_row)
    assert str(table) == "Col 1         \n--------------\nlong row value"
    for line in str(table).split("\n"):
        assert len(line) == len(long_row)


def test_table_prints_to_console_evenly_spaced_multi_column_long_row():
    long_row = "long row value"
    test_headers = ["Col 1", "Col 2"]
    test_row = [["a", long_row]]
    table = Table(test_headers, test_row)
    for line in str(table).split("\n"):
        assert len(line) == len(long_row) * 2 + 1


def test_table_prints_to_console_with_empty_input_arrays():
    test_headers = []
    test_row = []
    table = Table(test_headers, test_row)
    assert str(table) == "No table data."


def test_table_prints_to_console_with_empty_headers_array():
    test_headers = []
    test_row = [["a", "b"]]
    table = Table(test_headers, test_row)
    assert str(table) == "a|b"


def test_table_prints_to_console_with_empty_rows_array():
    test_headers = ["Col 1", "Col 2"]
    test_row = []
    table = Table(test_headers, test_row)
    assert str(table) == "Col 1|Col 2\n-----------"