from sqlfluff.dialects import dialect_snowflake
from sqlfluff.core.dialects import Dialect

def load_dialect() -> Dialect:
    # Copy Snowflake dialect and extend it
    dialect = dialect_snowflake.Dialect.copy_as("snowflake_with_iceberg")

    # Register custom grammar here
    from .iceberg_grammar import create_iceberg_table_segment
    dialect.add(create_iceberg_table_segment)

    return dialect
