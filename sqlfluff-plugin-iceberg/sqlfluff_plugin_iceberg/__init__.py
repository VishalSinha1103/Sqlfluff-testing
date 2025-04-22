"""SQLFluff Plugin for Snowflake CREATE ICEBERG TABLE support with a custom dialect."""

__version__ = "0.1.0"

from sqlfluff.core.plugin import hookimpl


@hookimpl
def get_dialect_plugins():
    """Get dialect plugins."""
    return [
        ("snowflake_with_iceberg", get_snowflake_with_iceberg_dialect)
    ]


def get_snowflake_with_iceberg_dialect():
    """Get a Snowflake dialect with ICEBERG TABLE support."""
    from sqlfluff.dialects import dialect_snowflake
    from sqlfluff.core.parser import (
        Sequence,
        OneOf,
        Ref,
        AnyNumberOf,
        StringParser,
        Bracketed,
        Delimited,
        OptionallyBracketed,
        ParseMode,
    )
    from sqlfluff.dialects import dialect_ansi as ansi
    
    # Create a new dialect class that inherits from SnowflakeDialect
    class SnowflakeWithIcebergDialect(dialect_snowflake.SnowflakeDialect):
        """Snowflake dialect with added support for ICEBERG TABLE syntax."""
        name = 'snowflake_with_iceberg'
        
        # We copy the inheritable elements from the parent class
        inheritable_lexer_matchers = dialect_snowflake.SnowflakeDialect.inheritable_lexer_matchers
        
        # Define the CREATE ICEBERG TABLE statement
        class CreateIcebergTableStatementSegment(ansi.CreateTableStatementSegment):
            """A `CREATE ICEBERG TABLE` statement for Snowflake."""
            type = 'create_iceberg_table_statement'
            match_grammar = Sequence(
                StringParser('CREATE', optional=False),
                Ref('OrReplaceGrammar', optional=True),
                Ref('TemporaryTransientGrammar', optional=True),
                StringParser('ICEBERG', optional=False),
                StringParser('TABLE', optional=False),
                Ref('IfNotExistsGrammar', optional=True),
                Ref('TableReferenceSegment', optional=False),
                OneOf(
                    # Columns and comment syntax:
                    Sequence(
                        Bracketed(
                            Delimited(
                                OneOf(
                                    Ref('TableConstraintSegment'),
                                    Ref('ColumnDefinitionSegment'),
                                ),
                                delimiter=Ref('CommaSegment'),
                                allow_trailing=True,
                            ),
                            parse_mode=ParseMode.GREEDY,
                        ),
                        Ref('TableConstraintSegment', optional=True),
                        Ref('CommentClauseSegment', optional=True),
                    ),
                    # Create AS syntax:
                    Sequence(
                        Ref('CommentClauseSegment', optional=True),
                        StringParser('AS', optional=False),
                        OptionallyBracketed(Ref('SelectableGrammar')),
                    ),
                    # Create like syntax
                    Sequence(
                        Ref('LikeClauseSegment', optional=True),
                        Ref('CommentClauseSegment', optional=True),
                    ),
                ),
                Ref('TableClusterBySegment', optional=True),
                AnyNumberOf(
                    Ref('TableEndClauseSegment'),
                    min_times=0,
                ),
            )
        
        # Override get_root_segments to include our new statement
        @classmethod
        def get_root_segments(cls):
            """Return the root segments for this dialect."""
            root_segments = super().get_root_segments()
            
            # Add our new segment if it's not already there
            for segment in root_segments:
                if getattr(segment, 'type', None) == 'create_iceberg_table_statement':
                    return root_segments
                    
            # Insert our segment after CreateTableStatementSegment
            for i, segment in enumerate(root_segments):
                if getattr(segment, '__name__', '') == 'CreateTableStatementSegment':
                    root_segments.insert(i + 1, cls.CreateIcebergTableStatementSegment)
                    break
                    
            return root_segments
    
    # Register our new segment with the dialect
    SnowflakeWithIcebergDialect.register(SnowflakeWithIcebergDialect.CreateIcebergTableStatementSegment)
    
    return SnowflakeWithIcebergDialect
