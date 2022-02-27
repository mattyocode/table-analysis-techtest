"""Table object."""

import operator


class Table:
    def __init__(self, headers, rows):
        self.cellwidths = {}
        self._headers = headers
        self._rows = []
        self.set_column_cell_widths(headers)
        if len(rows) > 0:
            for row in rows:
                self._rows.append(row)
                self.set_column_cell_widths(row)

    @property
    def headers(self):
        return self._headers

    @property
    def rows(self):
        return self._rows

    def set_column_cell_widths(self, cells):
        for i, cell in enumerate(cells):
            current_column_cellwidth = self.cellwidths.get(i, 0)
            self.cellwidths[i] = max(current_column_cellwidth, len(str(cell)))

    def __str__(self):
        """It prints each column to length of longest value in column, \
            i.e. column widths can differ from each other."""
        if len(self._headers) == 0 and len(self._rows) == 0:
            return "No table data."
        formatted = []
        if len(self._headers) > 0:
            formatted_headers = "|".join(
                [f"{header:{self.cellwidths[i]}}" for i, header in enumerate(self._headers)]
            )
            formatted.append(formatted_headers)
            formatted.append("-" * len(formatted_headers))
        for row in self.rows:
            formatted.append("|".join([f"{cell:{self.cellwidths[i]}}" for i, cell in enumerate(row)]))
        return "\n".join(formatted)

