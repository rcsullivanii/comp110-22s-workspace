"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730472431"

# Define your functions below


def read_csv_rows(data_file_path: str) -> list[dict[str, str]]:
    """Read the rows of a cvs into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(data_file_path, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    values: list[str] = []
    
    for row in rows:
        values.append(row[column])

    return values


def columnar(table_by_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    table_by_columns: dict[str, list[str]] = {}

    first_row: dict[str, str] = table_by_rows[0]
    for name in first_row:
        table_by_columns[name] = column_values(table_by_rows, name)

    return table_by_columns


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    revised: dict[str, list[str]] = {}

    for column in column_table:
        if (n >= len(column_table[column])):
            return column_table
        n_values: list[str] = []
        i: int = 0
        while (i < n):
            n_values.append(column_table[column][i])
            i += 1
        revised[column] = n_values

    return revised


def select(column_table: dict[str, list[str]], copied_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the orginal columns."""
    revised: dict[str, list[str]] = {}

    for name in copied_columns:
        revised[name] = column_table[name]

    return revised


def concat(col_t1: dict[str, list[str]], col_t2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    final: dict[str, list[str]] = {}

    for column in col_t1:
        final[column] = col_t1[column]

    for column in col_t2:
        if (column in final):
            final[column] += col_t2[column]
        else:
            final[column] = col_t2[column]

    return final


def count(values: list[str]) -> dict[str, int]:
    """Given a list, count produces a dict with count of how many times each key occurrs."""
    freq: dict[str, int] = {}
    for item in values:
        if item in freq:
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq


def threshold(count: dict[str, int], cutoff: int) -> int:
    """Creates a new dictionary which totals the number of counts in a dict that is modified via a threshold."""
    threshold: dict[str, int] = {}
    if (cutoff < 0 or cutoff > len(count)):
        return 0
    for keys in count:
        i: int = int(keys)
        if (i < cutoff):
            threshold[keys] = count[keys]
    sum: int = 0
    for keys in threshold:
        sum += threshold[keys]
    return sum