from sqlfluff.core.plugin import hookimpl
from sqlfluff.dialects.dialect_snowflake import dialect as snowflake_dialect
from .iceberg_grammar import CreateIcebergTableSegment

@hookimpl
def get_dialect_patch():
    dialect = snowflake_dialect.copy_as("snowflake_with_iceberg")
    dialect.replace(CreateIcebergTableSegment)
    return dialect
