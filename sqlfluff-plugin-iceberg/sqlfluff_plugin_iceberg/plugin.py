from sqlfluff.dialects import dialect_snowflake
from sqlfluff.core.dialects import Dialect

def load_dialect() -> Dialect:
    # Copy the base Snowflake dialect
    dialect = dialect_snowflake.Dialect.copy_as("snowflake_with_iceberg")

    # Import your custom iceberg grammar
    from .iceberg_grammar import create_iceberg_table_segment

    # Add the custom segment to the dialect
    dialect.add(create_iceberg_table_segment)

    return dialect
