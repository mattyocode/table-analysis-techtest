"""Command-line interface."""
import click

from .csv_loader import CSVLoader
from .query_helper import QueryHelper
from .table import Table


PRINT_EXCLUDE = [
    "Unit Name",
    "Property Address [1]",
    "Property  Address [2]",
    "Property Address [3]",
    "Property Address [4]",
    "Lease End Date",
]

# Functions that coordinate table queries for the command line.


def file_to_table(file_path):
    """Return table object with csv data from file."""
    csv_data = CSVLoader(file_path).data()
    table = Table(csv_data["headers"], csv_data["rows"])
    return table


def styled_title(title):
    """Helper that prints styled title to command line."""
    click.secho("-" * len(title), fg="green")
    click.secho(title, fg="green")
    click.secho("-" * len(title) + "\n", fg="green")


def smallest_by_value(table, amount, column_name):
    """Prints rows with smallest values to command line."""
    current_rent_smallest_5 = QueryHelper(table).smallest(amount, column_name)
    additional_exlude = ["Lease Start Date", "Lease Years"]
    current_rent_smallest_5.exclude_cols_from_print(PRINT_EXCLUDE + additional_exlude)

    title = f"Smallest {amount} values of {column_name} in ascending order."
    styled_title(title)
    click.echo(current_rent_smallest_5)
    click.echo("\n")


def masts_data_equals(table, value, column_name):
    """Prints rows where mast data equals value in column,
    and total value of those cells to command line."""
    filtered_table = table.get_rows_equal_to(column_name, value)
    total_rent = filtered_table.get_column_total("Current Rent")

    title = f"Mast data where {column_name} is equal to {value}. (All data fields.)"
    styled_title(title)
    click.echo(filtered_table)
    click.echo("\n")
    click.secho(f"Total rent: £{total_rent}", fg="blue")
    click.echo("\n")


def mast_count_dict(table, column_name):
    """Prints tenants with count of masts to command line."""
    frequency_dict = QueryHelper(table).frequency(column_name)
    title = "Count of masts by tenant."
    styled_title(title)
    for k, v in frequency_dict.items():
        click.echo(f"{k}: " + click.style(f"{v} masts", fg="blue"))
    click.echo("\n")


def mast_data_in_date_range(table, column_name, start_date, end_date):
    """Prints mast data where column values in date range to command line."""
    date_range_table = QueryHelper(table).dates_between(
        start_date, end_date, column_name
    )
    date_range_table.exclude_cols_from_print(PRINT_EXCLUDE)

    title = f"Mast data where {column_name} is between {start_date} and {end_date}"
    styled_title(title)
    click.echo(date_range_table)
    click.echo("\n")


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
    "--start-date-range",
    "-r",
    is_flag=True,
    help="Get mast data within start date range.",
)
def main(
    file_path, smallest_values, lease_years_equal, tenant_mast_count, start_date_range
):
    """Table Query Python Developer test."""
    table = file_to_table(file_path)

    run_all = not any(
        [smallest_values, lease_years_equal, tenant_mast_count, start_date_range]
    )

    if smallest_values or run_all:
        smallest_by_value(table, amount=5, column_name="Current Rent")

    if lease_years_equal or run_all:
        masts_data_equals(table, value="25", column_name="Lease Years")

    if tenant_mast_count or run_all:
        mast_count_dict(table, column_name="Tenant Name")

    if start_date_range or run_all:
        mast_data_in_date_range(
            table,
            column_name="Lease Start Date",
            start_date="01 Jun 1999",
            end_date="31 Aug 2007",
        )

    click.secho("Report finished!", fg="green")
