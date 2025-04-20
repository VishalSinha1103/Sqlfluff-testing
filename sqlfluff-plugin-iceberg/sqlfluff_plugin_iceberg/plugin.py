from sqlfluff.dialects import dialect_snowflake
from sqlfluff.core.dialects import Dialect

def load_dialect() -> Dialect:
    dialect = dialect_snowflake.Dialect.copy_as("snowflake_with_iceberg")
    # (register grammar additions here...)
    return dialect
