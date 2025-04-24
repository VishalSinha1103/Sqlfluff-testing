from sqlfluff.core.plugin import hookimpl
from sqlfluff_plugin_iceberg.dialect import iceberg_dialect

@hookimpl
def get_dialects():
    """Return Iceberg dialect."""
    return [iceberg_dialect]
