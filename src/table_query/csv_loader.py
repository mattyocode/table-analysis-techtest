"""Load CSV data into object."""
from csv import reader


class CSVLoader:
    """Class to handle reading csv data from file."""

    def __init__(self, file_path):
        self.file_path = file_path
        self._headers = []
        self._rows = []
        self.load_data()

    @property
    def headers(self):
        """Return table headers."""
        return self._headers

    @property
    def rows(self):
        """Return table rows."""
        return self._rows

    def load_data(self):
        """Load data from csv file into instance attributes."""
        with open(self.file_path) as csv_file:
            csv_reader = reader(csv_file)

            for i, row in enumerate(csv_reader):
                if i == 0:
                    self._headers = row
                else:
                    self._rows.append(row)

    def data(self):
        """Return dict with headers and row data."""
        return {"headers": self._headers, "rows": self._rows}
