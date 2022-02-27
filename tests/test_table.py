import pytest

from table_analyser.table import Table


def test_initalise_table_with_test_data():
    """It returns table object with test data for single column."""
    test_headers = ["Col 1"]
    test_row = [["a"]]
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row


def test_initalise_table_with_multi_column_test_data():
    """It returns table object with test data for two columns."""
    test_headers = ["Col 1", "Col 2"]
    test_row = [["a", "b"]]
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row


def test_initalise_table_with_multi_column_multi_row_test_data():
    """It returns table object with test data for two columns with two rows."""
    test_headers = ["Col 1", "Col 2"]
    test_rows = [["a", "b"], ["z", "y"]]
    table = Table(test_headers, test_rows)
    assert table.headers == test_headers
    assert table.rows == test_rows
    assert len(table.headers) == 2
    assert len(table.rows) == 2


def test_initialise_table_with_empty_input_arrays():
    """It returns table object when header and row are empty arrays."""
    test_headers = []
    test_row = []
    table = Table(test_headers, test_row)
    assert table.headers == test_headers
    assert table.rows == test_row


def test_table_prints_evenly_spaced_single_column():
    """It prints column with header and rows at length of longest value \
        with divider between header and row."""
    long_header = "Col 1"
    test_header = [long_header]
    test_row = [["a"]]
    table = Table(test_header, test_row)
    assert str(table) == "Col 1\n-----\na    "
    for line in str(table).split("\n"):
        assert len(line) == len(long_header)


def test_table_prints_evenly_spaced_columns_varying_lengths_long_header():
    """It prints each column to length of header when header \
        is longer than row cells."""
    test_headers = ["Col 1", "Col Two"]
    test_row = [["a", "bb"]]
    table = Table(test_headers, test_row)
    assert str(table) == "Col 1|Col Two\n-------------\na    |bb     "
    row_string = str(table).split("\n")[-1]
    first_cell, second_cell = row_string.split("|")
    assert len(first_cell) == len(test_headers[0])
    assert len(second_cell) == len(test_headers[1])


def test_table_prints_evenly_spaced_columns_varying_lengths_long_row_cell():
    """It prints each column to length of longest row cell \
        when row cell is longer than header."""
    test_headers = ["Col 1", "Col 2"]
    test_row = [["long val", "longer value"]]
    table = Table(test_headers, test_row)
    assert str(table) == "Col 1   |Col 2       \n---------------------\nlong val|longer value"
    header_string = str(table).split("\n")[0]
    first_header, second_header = header_string.split("|")
    assert len(first_header) == len(test_row[0][0])
    assert len(second_header) == len(test_row[0][1])


def test_table_prints_with_empty_input_arrays():
    test_headers = []
    test_row = []
    table = Table(test_headers, test_row)
    assert str(table) == "No table data."


def test_table_prints_with_empty_headers_array():
    test_headers = []
    test_row = [["a", "b"]]
    table = Table(test_headers, test_row)
    assert str(table) == "a|b"


def test_table_prints_with_empty_rows_array():
    test_headers = ["Col 1", "Col 2"]
    test_row = []
    table = Table(test_headers, test_row)
    assert str(table) == "Col 1|Col 2\n-----------"
