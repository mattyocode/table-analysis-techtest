from unittest.mock import patch 

import pytest

from table_query.query_helper import QueryHelper
from table_query.table import Table


# @pytest.fixture
# def table():
#     table = Table([], [])
#     return table


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
    table = Table(TEST_TABLE_HEADERS,TEST_TABLE_ROWS)
    result_table = QueryHelper(table).get_smallest(5, "Col 3")
    assert result_table.headers == TEST_TABLE_HEADERS
    assert result_table.rows == [
        ["f", 6, 5.2],
        ["e", 5, 17.9],
        ["c", 3, 18.0],
        ["d", 4, 27.9],
        ["b", 2, 37.9],
    ]
