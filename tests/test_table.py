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
    """It returns `No table data.` message when empty arrays supplied \
        for headers and rows."""
    test_headers = []
    test_row = []
    table = Table(test_headers, test_row)
    assert str(table) == "No table data."


def test_table_prints_with_empty_headers_array():
    """It returns row data only when empty array supplied for headers."""
    test_headers = []
    test_row = [["a", "b"]]
    table = Table(test_headers, test_row)
    assert str(table) == "a|b"


def test_table_prints_with_empty_rows_array():
    """It returns header data only when empty array supplied for rows."""
    test_headers = ["Col 1", "Col 2"]
    test_row = []
    table = Table(test_headers, test_row)
    assert str(table) == "Col 1|Col 2\n-----------"


def test_table_returns_new_table_sorted_by_integer_column_value():
    """It returns new table object sorted by integers (ascending) in given column."""
    test_headers = ["Col 1", "Col 2"]
    test_rows = [[5, 4], [1, 6]]
    table = Table(test_headers, test_rows)
    sorted_table = table.sort_by("Col 1")
    assert sorted_table.rows == [[1, 6], [5, 4]]


def test_table_returns_new_table_with_same_order_when_integers_already_sorted():
    """It returns new table object unchanged if given column of integers is already sorted."""
    test_headers = ["Col 1", "Col 2"]
    test_rows = [[5, 4], [1, 6]]
    table = Table(test_headers, test_rows)
    sorted_table = table.sort_by("Col 2")
    assert sorted_table.rows == [[5, 4], [1, 6]]


def test_table_returns_new_table_sorted_by_string_column_value():
    """It returns new table object sorted by string (ascending) in given column."""
    test_headers = ["Col 1", "Col 2"]
    test_rows = [["x", "y"], ["a", "b"]]
    table = Table(test_headers, test_rows)
    sorted_table = table.sort_by("Col 1")
    assert sorted_table.rows == [["a", "b"], ["x", "y"]]


def test_table_returns_new_table_with_same_order_when_strings_already_sorted():
    """It returns new table object unchanged if given column of strings is already sorted."""
    test_headers = ["Col 1", "Col 2"]
    test_rows = [["a", "b"], ["x", "y"]]
    table = Table(test_headers, test_rows)
    sorted_table = table.sort_by("Col 1")
    assert sorted_table.rows == [["a", "b"], ["x", "y"]]


