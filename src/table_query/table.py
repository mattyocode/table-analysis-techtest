from datetime import datetime


class Table:
    """Class to handle tabular data.
    Creates dict of column widths on initialization for better printing.
    """

    def __init__(self, headers, rows):
        self.cellwidths = {}
        self._headers = headers
        self._rows = []
        self._excluded_from_print = []
        self.set_column_cell_widths(headers)
        if len(rows) > 0:
            for row in rows:
                self._rows.append(row)
                self.set_column_cell_widths(row)

    def set_column_cell_widths(self, cells):
        """Iterate through array and set cellwidths dictionary to 
        max width of each column. Helper function for initialisation."""
        for i, cell in enumerate(cells):
            current_column_cellwidth = self.cellwidths.get(i, 0)
            self.cellwidths[i] = max(current_column_cellwidth, len(str(cell)))

    @property
    def headers(self):
        """Return table headers."""
        return self._headers

    @property
    def rows(self):
        """Return table rows."""
        return self._rows

    @property
    def excluded_from_print(self):
        """Return columns exluded from printing."""
        return self._excluded_from_print

    def exclude_cols_from_print(self, columns):
        """Add list of column names to attributes.
        Column nanme is stored as index so it can be
        used while iterating over both headers and rows.
        """
        for column_name in columns:
            column_index = self._headers.index(column_name)
            self._excluded_from_print.append(column_index)
        return self._excluded_from_print

    def __str__(self):
        """It returns table data in grid format, with each 
        column the width of its longest cell.
        """
        if len(self._headers) == 0 and len(self._rows) == 0:
            return "No table data."
        formatted = []
        if len(self._headers) > 0:
            formatted_headers = "|".join(
                [
                    f"{header:{self.cellwidths[i]}}"
                    for i, header in enumerate(self._headers)
                    if i not in self._excluded_from_print
                ]
            )
            formatted.append(formatted_headers)
            formatted.append("-" * len(formatted_headers))
        for row in self.rows:
            formatted.append(
                "|".join(
                    [
                        f"{cell:{self.cellwidths[i]}}"
                        for i, cell in enumerate(row)
                        if i not in self._excluded_from_print
                    ]
                )
            )
        return "\n".join(formatted)


    def sort_by(self, column_name):
        """Return new table sorted by given column of float or int."""
        column_index = self._headers.index(column_name)
        return Table(
            self.headers, sorted(self.rows, key=lambda x: float(x[column_index]))
        )


    def get_column_total(self, column_name):
        """Return total value for numerical column."""
        total = 0
        column_index = self._headers.index(column_name)
        for row in self._rows:
            total += float(row[column_index])
        return total

    def get_rows_equal_to(self, column_name, value):
        """Return new table object with rows matching value.
            Using list comprehension here to meet requirements
            and as data set is small but implementing binary
            search would be more performant."""
        column_index = self._headers.index(column_name)
        return Table(
            self._headers, [row for row in self._rows if row[column_index] == value]
        )

    def get_rows_between(self, column_name, start_value, end_value):
        """Return new table object with rows between required values - inclusive. \
            As above, implementation isn't optimsed."""
        column_index = self._headers.index(column_name)
        return Table(
            self._headers,
            [
                row
                for row in self._rows
                if row[column_index] >= start_value and row[column_index] <= end_value
            ],
        )

    def string_column_to_datetime(self, column_name):
        """Return table with column converted to datetime object in place."""
        column_index = self._headers.index(column_name)
        for row in self._rows:
            row[column_index] = datetime.strptime(row[column_index], "%d %b %Y").date()
        return self


    def datetime_column_to_string(self, column_name):
        """Return table with column converted string format DD/MM/YYYY."""
        column_index = self._headers.index(column_name)
        for row in self._rows:
            row[column_index] = datetime.strftime(row[column_index], "%d/%m/%Y")
        return self
