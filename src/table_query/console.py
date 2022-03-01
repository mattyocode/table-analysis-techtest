import click

from .csv_loader import CSVLoader
from .table import Table
from .query_helper import QueryHelper

def file_to_table(file_path):
	csv_data = CSVLoader(file_path)
	table = Table(csv_data.headers, csv_data.rows)
	return table


def smallest_by_value(table, number, column_name):
		current_rent_smallest_5 = QueryHelper(table).smallest(number, column_name)
		
		click.echo(f"Smallest {number} values of {column_name} in ascending order\n")
		click.echo(current_rent_smallest_5)


@click.command()
@click.option("--file-path", "-f", type=click.Path(exists=True), default="fixtures/Python Developer Test Dataset.csv")
@click.option("--smallest-values", "-s", is_flag=True, help="Get smallest values only.")
def main(file_path, smallest_values):
    """Table Analysis Python Developer test."""
    table = file_to_table(file_path)

    if smallest_values:
        smallest_by_value(table, number = 5, column_name = "current rent")

    click.echo("Hello world!")
