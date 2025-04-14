from sqlfluff.core.parser import (
    BaseSegment,
    Sequence,
    Indent,
    Dedent,
    Bracketed,
    Delimited,
    Ref,
)

class CreateIcebergTableSegment(BaseSegment):
    """A `CREATE ICEBERG TABLE` statement."""

    type = "create_iceberg_table_statement"

    match_grammar = Sequence(
        "CREATE",
        "ICEBERG",
        "TABLE",
        Indent,
        Ref("TableReferenceSegment"),
        Bracketed(
            Delimited(
                Ref("ColumnDefinitionSegment")
            )
        ),
        Dedent
    )
