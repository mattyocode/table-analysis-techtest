"""Table object."""

import operator

class Table():
    def __init__(self, headers, rows):
        self.cellwidth = 0
        self._headers = headers
        for header in headers:
            self.cellwidth = self.longest_cellwidth(header)
        self._rows = []
        if len(rows) > 0:
            for row in rows:
                self._rows.append(row)
                for cell in row:
                    self.cellwidth = self.longest_cellwidth(cell)

    @property
    def headers(self):
        return self._headers

    @property
    def rows(self):
        return self._rows

    def longest_cellwidth(self, cell):
        return max(len(str(cell)), self.cellwidth)

    def __str__(self):
        if len(self._headers) == 0 and len(self._rows) == 0:
            return "No table data."
        formatted = []
        if len(self._headers) > 0:
            formatted_headers = "|".join([f"{header:{self.cellwidth}}" for header in self._headers])
            formatted.append(formatted_headers)
            formatted.append("-" * len(formatted_headers))
        for row in self.rows:
            formatted.append("|".join([f"{cell:{self.cellwidth}}" for cell in row]))
        return "\n".join(formatted)