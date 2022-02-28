"""CSVLoader object."""
from csv import reader
import enum

class CSVLoader():
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

    def load_csv(self):
        with open(self.file_path) as csv_file:
            csv_reader = reader(csv_file)
        return csv_reader

    def load_data(self):
        csv_reader = self.load_csv()

        for i, row in enumerate(csv_reader):
            if i == 0:
                self._headers = row
            else:
                self._rows.append(row)

    def data(self):
        return {
            "headers": self._headers, 
            "rows": self._rows
        }
