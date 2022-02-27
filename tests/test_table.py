import pytest

from table_analyser.table import Table


def test_initalise_table_with_test_data():
    test_headers = ["Col 1"]
    test_row = [["a"]]
    table = Table(test_headers, test_row)
    assert table.headers == ["Col 1"]
    assert table.rows == [["a"]]

