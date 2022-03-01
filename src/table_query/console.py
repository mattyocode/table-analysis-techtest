import click

from .csv_loader import CSVLoader
from .table import Table
from .query_helper import QueryHelper

def file_to_table(file_path):
	csv_data = CSVLoader(file_path)
	table = Table(csv_data.headers, csv_data.rows)
	return table


@click.command()
@click.option("--file-path", "-f", type=click.Path(exists=True), default="fixtures/Python Developer Test Dataset.csv")
def main(file_path):
    """Table Analysis Python Developer test."""
    table = file_to_table(file_path)
    click.echo("Hello world!")
