import csv
import json
from pathlib import Path


class DataFrame:
    """
    Lightweight, pure Python class that mimics Spark DataFrame APIs
    for local processing without Spark JVM dependencies.
    """

    def __init__(self, columns: list, rows: list):
        self.columns = columns
        self.rows = rows  # List of dictionaries, each matching columns

    @property
    def rdd(self):
        # Mimics the df.rdd interface
        class RDDMock:
            def __init__(self, rows):
                self.isEmpty = len(rows) == 0
        return RDDMock(self.rows)

    def first(self) -> dict:
        if not self.rows:
            raise IndexError("DataFrame is empty")
        return self.rows[0]

    def filter(self, func) -> 'DataFrame':
        """
        Supports passing a custom lambda function to filter rows
        """
        filtered_rows = [r for r in self.rows if func(r)]
        return DataFrame(self.columns, filtered_rows)

    def select(self, *cols) -> 'DataFrame':
        """
        Filters columns to keep only the selected ones
        """
        selected_cols = list(cols)
        # Handle unpacking if list of columns is passed
        if len(selected_cols) == 1 and isinstance(selected_cols[0], (list, tuple)):
            selected_cols = list(selected_cols[0])

        new_rows = []
        for r in self.rows:
            new_rows.append({c: r.get(c, "") for c in selected_cols})
        return DataFrame(selected_cols, new_rows)

    def withColumn(self, col_name: str, value_expr) -> 'DataFrame':
        """
        Adds or overrides a column. value_expr can be a scalar or a callable lambda.
        """
        new_cols = list(self.columns)
        if col_name not in new_cols:
            new_cols.append(col_name)

        new_rows = []
        for r in self.rows:
            new_row = dict(r)
            if callable(value_expr):
                new_row[col_name] = value_expr(new_row)
            else:
                new_row[col_name] = value_expr
            new_rows.append(new_row)
        return DataFrame(new_cols, new_rows)

    def count(self) -> int:
        return len(self.rows)

    @property
    def write(self):
        outer_self = self

        class DataFrameWriter:
            def __init__(self):
                self._format = "csv"
                self._mode = "overwrite"
                self._partitions = []

            def format(self, fmt: str):
                self._format = fmt
                return self

            def mode(self, md: str):
                self._mode = md
                return self

            def partitionBy(self, *cols):
                self._partitions = list(cols)
                return self

            def save(self, output_path: str):
                path = Path(output_path)
                # Create parent folders
                path.parent.mkdir(parents=True, exist_ok=True)

                # If it's a directory, write a standard csv/parquet file inside
                if path.is_dir() or not path.suffix:
                    path.mkdir(parents=True, exist_ok=True)
                    path = path / "part-00000.csv"

                # Write as flat CSV representing our structured columns
                with open(path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=outer_self.columns)
                    writer.writeheader()
                    for r in outer_self.rows:
                        # Ensure row dict only contains our defined columns
                        writer.writerow({c: r.get(c, "") for c in outer_self.columns})

        return DataFrameWriter()


def path_exists(path_str: str) -> bool:
    """
    Checks if a file or directory path exists using pathlib.Path
    """
    if not path_str:
        return False
    return Path(path_str).exists()


def _load_schema_fields(schema_path: str) -> list:
    """
    Loads columns from JSON validation schema file, ignoring 'TEMPLATE'
    """
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_data = json.load(f)
    column_names = schema_data.get("columnNames", [])
    # Filter out TEMPLATE column
    fields = [c.get("FieldName", "").strip() for c in column_names if c.get("FieldName", "") != "TEMPLATE"]
    return fields


def delimitedFile(file_path: str, schema_path: str, has_header: str, delimiter: str, quote_char: str = '"') -> DataFrame:
    """
    Reads a delimited CSV file using the JSON validation schema
    """
    fields = _load_schema_fields(schema_path)

    rows = []
    # Set standard default quote if empty
    q = quote_char if quote_char else '"'
    d = delimiter if delimiter else ','

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=d, quotechar=q)
        raw_rows = list(reader)

    # Skip header row if has_header is True
    start_idx = 1 if str(has_header).lower() == "true" and raw_rows else 0

    for raw_row in raw_rows[start_idx:]:
        row_dict = {}
        for idx, field in enumerate(fields):
            row_dict[field] = raw_row[idx] if idx < len(raw_row) else ""
        rows.append(row_dict)

    return DataFrame(fields, rows)


def withoutHeader(file_path: str, schema_path: str, delimiter: str, quote_char: str = '"') -> DataFrame:
    """
    Reads a delimited CSV file without header
    """
    return delimitedFile(file_path, schema_path, "False", delimiter, quote_char)


def isIgnoreHeader(file_path: str, schema_path: str, delimiter: str, quote_char: str = '"') -> DataFrame:
    """
    Reads a delimited CSV file and ignores the first row (the header)
    """
    return delimitedFile(file_path, schema_path, "True", delimiter, quote_char)
