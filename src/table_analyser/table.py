"""Table object."""

import operator

class Table():
    def __init__(self, headers, rows):
        self._headers = headers
        self._rows = []
        for row in rows:
            self._rows.append(row)

    @property
    def headers(self):
        return self._headers

    @property
    def rows(self):
        return self._rows