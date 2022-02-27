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


def test_initialise_empty_table_with_empty_arrays():
    test_headers = []
    test_row = []
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row

