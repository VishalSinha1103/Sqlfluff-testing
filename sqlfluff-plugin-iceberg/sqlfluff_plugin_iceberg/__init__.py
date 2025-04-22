"""SQLFluff Plugin for Snowflake CREATE TABLE ... USING ICEBERG support."""

__version__ = "0.1.0"

from sqlfluff.core.plugin import hookimpl


@hookimpl
def get_dialect_plugins():
    """Get dialect plugins."""
    return [
        ("snowflake_with_iceberg", get_snowflake_with_iceberg_dialect)
    ]


def get_snowflake_with_iceberg_dialect():
    """Get a Snowflake dialect with ICEBERG support."""
    from sqlfluff.dialects import dialect_snowflake
    from sqlfluff.core.parser import (
        Sequence,
        OneOf,
        Ref,
        AnyNumberOf,
        StringParser,
        Bracketed,
        Delimited,
        ParseMode,
        BaseSegment,
    )

    from sqlfluff.dialects import dialect_ansi as ansi

    # Define USING ICEBERG clause
    class UsingIcebergClauseSegment(BaseSegment):
        """`USING ICEBERG` clause."""
        type = "using_iceberg_clause"
        match_grammar = Sequence(
            StringParser("USING", optional=False),
            StringParser("ICEBERG", optional=False),
        )

    # Register new segment
    class SnowflakeWithIcebergDialect(dialect_snowflake.SnowflakeDialect):
        """Snowflake dialect with support for USING ICEBERG clause."""
        name = "snowflake_with_iceberg"

    SnowflakeWithIcebergDialect.register(UsingIcebergClauseSegment)

    # Extend CreateTableStatementSegment
    class CreateTableWithIcebergSegment(dialect_snowflake.CreateTableStatementSegment):
        """A `CREATE TABLE` statement with optional `USING ICEBERG`."""
        type = "create_table_statement"
        match_grammar = Sequence(
            OneOf("CREATE", Sequence("CREATE", "OR", "REPLACE")),
            Ref("TemporaryTransientGrammar", optional=True),
            "TABLE",
            Ref("IfNotExistsGrammar", optional=True),
            Ref("TableReferenceSegment"),
            Bracketed(
                Delimited(
                    OneOf(
                        Ref("ColumnDefinitionSegment"),
                        Ref("TableConstraintSegment"),
                    ),
                    delimiter=Ref("CommaSegment"),
                    allow_trailing=True,
                ),
                parse_mode=ParseMode.GREEDY,
            ),
            Ref("CommentClauseSegment", optional=True),
            Ref("UsingIcebergClauseSegment", optional=True),  # <<< KEY LINE
            Ref("TableClusterBySegment", optional=True),
            AnyNumberOf(
                Ref("TableEndClauseSegment"),
                min_times=0,
            ),
        )

    SnowflakeWithIcebergDialect.register(CreateTableWithIcebergSegment)

    return SnowflakeWithIcebergDialect
