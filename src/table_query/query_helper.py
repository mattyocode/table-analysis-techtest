from datetime import datetime

from table_query.table import Table


class QueryHelper:
    """Class to undertake (slightly) more complex queries on Tables."""

    def __init__(self, table):
        self.table = table

    def smallest(self, amount, column_name):
        """Return smallest values from rows sorted in ascending order.
        Column value must be number, float, or numerical string."""
        sorted_table = self.table.sort_by(column_name)
        return Table(sorted_table.headers, sorted_table.rows[:amount])

    def frequency(self, column_name):
        """Return historgram dict of value occurrences in column."""
        value_occurances = {}
        column_index = self.table.headers.index(column_name)
        rows = self.table.rows
        for row in rows:
            value = row[column_index]
            value_occurances[value] = value_occurances.get(value, 0) + 1
        return value_occurances

    def dates_between(self, start_date, end_date, column_name):
        """Return table with rows in date range."""
        self.table.string_column_to_datetime(column_name)
        start_date_datetime = datetime.strptime(start_date, "%d %b %Y").date()
        end_date_datetime = datetime.strptime(end_date, "%d %b %Y").date()
        table_in_range = self.table.get_rows_between(
            column_name, start_date_datetime, end_date_datetime
        )
        return table_in_range.datetime_column_to_string(column_name)
