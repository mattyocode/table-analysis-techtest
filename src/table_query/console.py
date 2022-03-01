import click

from .csv_loader import CSVLoader
from .query_helper import QueryHelper
from .table import Table


def file_to_table(file_path):
    csv_data = CSVLoader(file_path).data()
    table = Table(csv_data["headers"], csv_data["rows"])
    return table


def smallest_by_value(table, number, column_name):
    current_rent_smallest_5 = QueryHelper(table).smallest(number, column_name)

    click.echo(f"Smallest {number} values of {column_name} in ascending order\n")
    click.echo(current_rent_smallest_5)


def masts_data_equals(table, value, column_name):
    filtered_table = table.get_rows_equal_to(column_name, value)
    total_rent = filtered_table.get_column_total("Current Rent")

    click.echo(f"Mast data where {column_name} is equal to {value}\n")
    click.echo(filtered_table)
    click.echo(f"Total rent: £{total_rent}")


def mast_count_dict(table, column_name):
    frequency_dict = QueryHelper(table).frequency(column_name)

    click.echo("Count of masts by tenant\n")
    for k, v in frequency_dict.items():
        click.echo(f"{k}: {v} masts\n")


def mast_data_in_date_range(table, column_name, start_date, end_date):
    date_range_table = QueryHelper(table).dates_between(start_date, end_date)

    click.echo(
        f"Mast data where {column_name} is between {start_date} and {end_date}\n"
    )
    click.echo(date_range_table)


@click.command()
@click.option(
    "--file-path",
    "-f",
    type=click.Path(exists=True),
    default="fixtures/Python Developer Test Dataset.csv",
)
@click.option("--smallest-values", "-s", is_flag=True, help="Get smallest values only.")
@click.option(
    "--lease-years-equal",
    "-l",
    is_flag=True,
    help="Get lease years equal to value only.",
)
@click.option(
    "--tenant-mast-count",
    "-t",
    is_flag=True,
    help="Get mast count by tenant.",
)
@click.option(
    "--start_date_range",
    "-s",
    is_flag=True,
    help="Get mast data within start date range.",
)
def main(
    file_path, smallest_values, lease_years_equal, tenant_mast_count, start_date_range
):
    """Table Query Python Developer test."""
    table = file_to_table(file_path)

    if smallest_values:
        smallest_by_value(table, number=5, column_name="Current Rent")

    if lease_years_equal:
        masts_data_equals(table, value=25, column_name="Lease Years")

    if tenant_mast_count:
        mast_count_dict(table, column_name="Tenant Name")

    if start_date_range:
        mast_data_in_date_range(
            table,
            column_name="Lease Start Date",
            start_date="01 Jun 1999",
            end_date="31 Aug 2007",
        )

    click.echo("Report finished!")
