# from unittest.mock import patch

import pytest

from table_query.query_helper import QueryHelper
from table_query.table import Table

TEST_TABLE_HEADERS = ["Col 1", "Col 2", "Col 3"]
TEST_TABLE_ROWS = [
    ["a", 1, 42.4],
    ["b", 2, 37.9],
    ["c", 3, 18.0],
    ["d", 4, 27.9],
    ["e", 5, 17.9],
    ["f", 6, 5.2],
]


def test_get_5_smallest_values_in_column():
    """It returns table object with 5 smallest values by column."""
    table = Table(TEST_TABLE_HEADERS, TEST_TABLE_ROWS)
    result_table = QueryHelper(table).smallest(5, "Col 3")
    assert result_table.headers == TEST_TABLE_HEADERS
    assert result_table.rows == [
        ["f", 6, 5.2],
        ["e", 5, 17.9],
        ["c", 3, 18.0],
        ["d", 4, 27.9],
        ["b", 2, 37.9],
    ]


def test_raise_error_when_smallest_called_on_table_without_stated_column():
    """It raises error if column does not exist."""
    table = Table([], [])
    with pytest.raises(ValueError):
        QueryHelper(table).smallest(5, "Col 3")


def test_get_frequency_for_column_value():
    """It returns dict totalling occurances of same values in a column."""
    repeat_values = [["d", 0, 0], ["d", 0, 0], ["a", 0, 0]]
    test_rows_with_repeats = TEST_TABLE_ROWS + repeat_values
    table = Table(TEST_TABLE_HEADERS, test_rows_with_repeats)
    results_dict = QueryHelper(table).frequency("Col 1")
    assert results_dict == {"a": 2, "b": 1, "c": 1, "d": 3, "e": 1, "f": 1}


def test_raise_error_when_frequency_called_on_table_without_stated_column():
    """It raises error if column does not exist."""
    table = Table([], [])
    with pytest.raises(ValueError):
        QueryHelper(table).frequency("Col 1")


def test_get_rows_in_date_range():
    """It returns rows within date range, inclusive."""
    row_with_dates = [
        ["a", 1, "01 Mar 1994"],
        ["b", 2, "01 Jun 1999"],
        ["c", 3, "28 Nov 2000"],
        ["d", 4, "05 May 2005"],
        ["e", 5, "31 Aug 2007"],
        ["f", 6, "01 Sep 2007"],
    ]
    table = Table(TEST_TABLE_HEADERS, row_with_dates)
    results_table = QueryHelper(table).dates_between(
        "01 Jun 1999", "31 Aug 2007", "Col 3"
    )
    assert results_table.rows == [
        ["b", 2, "01/06/1999"],
        ["c", 3, "28/11/2000"],
        ["d", 4, "05/05/2005"],
        ["e", 5, "31/08/2007"],
    ]


# def test_get_all_data_where_value_equals_amount():
#     """It returns table object with rows equal to stated value. """
#     test_rows_with_double = TEST_TABLE_ROWS + ["y", 5, 0]
#     table = Table(TEST_TABLE_HEADERS,test_rows_with_double)
#     result_table = QueryHelper(table).get_matches_where("Col 2", 5)
#     assert result_table.headers == TEST_TABLE_HEADERS
