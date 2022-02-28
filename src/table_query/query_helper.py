"""QueryHelper class to perform more complex queries on Table."""
from table_query.table import Table


class QueryHelper():

    def __init__(self, table):
        self.table = table

    def get_smallest(self, amount, column_name):
        print(self.table)
        sorted_table = self.table.sort_by(column_name)
        return Table(sorted_table.headers, sorted_table.rows[:amount])
