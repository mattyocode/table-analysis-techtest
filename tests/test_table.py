import datetime

import pytest

from table_query.table import Table


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
    assert (
        str(table)
        == "Col 1   |Col 2       \n---------------------\nlong val|longer value"
    )

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


def test_get_excluded_column_indexes():
    """It returns list of indexes of excluded columns."""
    test_headers = ["Col 1", "Col 2"]
    test_row = []
    table = Table(test_headers, test_row)
    table.exclude_cols_from_print(["Col 1"])
    assert table.excluded_from_print == [0]


def test_table_doesnt_print_excluded_columns():
    """It doesn't print columns added to exclude list."""
    test_headers = ["FirstCol", "SecondCol", "ThirdCol"]
    test_row = [["aa", "bb", "cc"], ["dd", "ee", "ff"]]
    table = Table(test_headers, test_row)
    assert table.rows == [["aa", "bb", "cc"], ["dd", "ee", "ff"]]
    table.exclude_cols_from_print(["SecondCol", "ThirdCol"])
    excluded_values = ["SecondCol", "ThirdCol", "bb", "cc", "ee", "ff"]
    assert not any(x in str(table) for x in excluded_values)


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


def test_table_raises_valueerror_if_sort_by_called_on_non_numerical_string():
    """It raises ValueError if string cannot be converted to float."""
    test_headers = ["Col 1", "Col 2"]
    test_rows = [["a", "b"], ["x", "y"]]
    table = Table(test_headers, test_rows)
    with pytest.raises(ValueError):
        table.sort_by("Col 1")


def test_convert_date_string_to_datetime_object():
    """It returns table with selected column converted to datetime.date object."""
    test_header = ["Date field"]
    test_row = [["28 Apr 2018"]]
    table = Table(test_header, test_row)
    table.string_column_to_datetime("Date field")
    assert type(table.rows[0][0]) == datetime.date
    assert table.rows[0][0] == datetime.date(2018, 4, 28)


def test_convert_date_string_to_datetime_object_multi_row_multi_column():
    """It returns table with selected column converted to datetime.date object."""
    test_header = ["Name", "Date field"]
    test_row = [["Tony", "28 Apr 2018"], ["Paulie", "5 Nov 2012"]]
    table = Table(test_header, test_row)
    table.string_column_to_datetime("Date field")
    assert table.rows[0][1] == datetime.date(2018, 4, 28)
    assert table.rows[1][1] == datetime.date(2012, 11, 5)


def test_convert_datetime_object_to_date_string():
    """It returns table with selected column as date strings with DD/MM/YYYY format."""
    datetime_object = datetime.date(2018, 4, 28)
    test_header = ["Date field"]
    test_row = [[datetime_object]]
    table = Table(test_header, test_row)
    table.datetime_column_to_string("Date field")
    assert type(table.rows[0][0]) == str
    assert table.rows[0][0] == "28/04/2018"


def test_convert_datetime_object_to_date_string_multi_row_multi_column():
    """It returns table with selected column as date strings, other columns remain the same."""
    datetime_object_1 = datetime.date(2018, 4, 28)
    datetime_object_2 = datetime.date(2012, 11, 5)
    test_header = ["Name", "Date field"]
    test_row = [["Tony", datetime_object_1], ["Paulie", datetime_object_2]]
    table = Table(test_header, test_row)
    table.datetime_column_to_string("Date field")
    assert table.rows[0][1] == "28/04/2018"
    assert table.rows[1][1] == "05/11/2012"


def test_throws_error_if_column_values_are_not_of_type_string():
    """It throws TypeError if provided with non-string input."""
    test_header = ["Numeric value"]
    test_row = [[1]]
    table = Table(test_header, test_row)
    with pytest.raises(TypeError):
        table.string_column_to_datetime("Numeric value")


def test_throws_error_if_date_string_incorrectly_formatted():
    """It throws ValueError if provided with incorrectly formatted date string input."""
    test_header = ["Date field"]
    test_row = [["Apr 28 2018"]]
    table = Table(test_header, test_row)
    with pytest.raises(ValueError):
        table.string_column_to_datetime("Date field")


def test_get_integer_column_total_value():
    """It returns total value of column of integers."""
    test_header = ["Amounts"]
    test_row = [[1], [2], [3]]
    table = Table(test_header, test_row)
    result = table.get_column_total("Amounts")
    assert result == 1 + 2 + 3


def test_get_float_column_total_value():
    """It returns total value of column of floats."""
    test_header = ["Amounts"]
    test_row = [[1.2], [2.4], [3.3]]
    table = Table(test_header, test_row)
    result = table.get_column_total("Amounts")
    assert result == 1.2 + 2.4 + 3.3


def test_throws_error_when_values_are_strings():
    """It throws error when attempting to return total value \
        of column of non-numeric strings."""
    test_header = ["Amounts"]
    test_row = [["One"], ["Two"], ["Three"]]
    table = Table(test_header, test_row)
    with pytest.raises(ValueError):
        table.get_column_total("Amounts")


def test_table_returns_rows_equal_to_given_value_in_column_single_match():
    """It returns a new table object with single row equal to given value \
        in given column when only one match exists."""
    test_headers = ["Name", "Amount"]
    test_rows = [["Tony", 10], ["Paulie", 20]]
    table = Table(test_headers, test_rows)
    filtered_table = table.get_rows_equal_to("Amount", 20)
    assert filtered_table.rows == [["Paulie", 20]]


def test_table_returns_rows_equal_to_given_value_in_column_multi_match():
    """It returns a new table object with rows equal to given value \
        in given column when multiple rows match value."""
    test_headers = ["Name", "Amount"]
    test_rows = [["Tony", 10], ["Paulie", 20], ["Chris", 20]]
    table = Table(test_headers, test_rows)
    filtered_table = table.get_rows_equal_to("Amount", 20)
    assert filtered_table.rows == [["Paulie", 20], ["Chris", 20]]


def test_return_empty_table_if_no_rows_match_requirements():
    """It returns a new empty table object when no rows match given value."""
    test_headers = ["Name", "Amount"]
    test_rows = [["Tony", 10], ["Paulie", 20], ["Chris", 20]]
    table = Table(test_headers, test_rows)
    filtered_table = table.get_rows_equal_to("Amount", 30)
    assert filtered_table.rows == []


def test_table_returns_rows_between_value_range():
    """It returns a new table object with rows between to given value \
        in given column."""
    test_headers = ["Name", "Amount"]
    test_rows = [["Tony", 10], ["Paulie", 20], ["Chris", 25]]
    table = Table(test_headers, test_rows)
    filtered_table = table.get_rows_between("Amount", 20, 25)
    assert filtered_table.rows == [["Paulie", 20], ["Chris", 25]]


def test_table_returns_empty_table_if_no_rows_between_value_range():
    """It returns a new empty table object when no rows in given range."""
    test_headers = ["Name", "Amount"]
    test_rows = [["Tony", 10], ["Paulie", 20], ["Chris", 25]]
    table = Table(test_headers, test_rows)
    filtered_table = table.get_rows_between("Amount", 28, 30)
    assert filtered_table.rows == []
