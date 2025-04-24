from sqlfluff.core.dialects import load_raw_dialect
from sqlfluff.core.parser import (
    Sequence, OneOf, Ref, KeywordSegment, 
    Bracketed, Anything, StringParser
)

# Load the base MySQL dialect
mysql_dialect = load_raw_dialect("mysql")

# Define Iceberg-specific keyword
class IcebergKeywordSegment(KeywordSegment):
    """The ICEBERG keyword."""
    match_grammar = StringParser("ICEBERG", KeywordSegment.type)

# Define other Iceberg-specific keywords
class CatalogKeywordSegment(KeywordSegment):
    """The CATALOG keyword."""
    match_grammar = StringParser("CATALOG", KeywordSegment.type)

class ExternalVolumeKeywordSegment(KeywordSegment):
    """The EXTERNAL_VOLUME keyword."""
    match_grammar = StringParser("EXTERNAL_VOLUME", KeywordSegment.type)

class BaseLocationKeywordSegment(KeywordSegment):
    """The BASE_LOCATION keyword."""
    match_grammar = StringParser("BASE_LOCATION", KeywordSegment.type)

# Create a custom iceberg dialect
iceberg_dialect = mysql_dialect.copy_as("iceberg")

# Add ICEBERG keyword to CREATE TABLE syntax
create_table_segment = iceberg_dialect.get_segment("CreateTableStatementSegment")
create_grammar_first_part = create_table_segment.match_grammar.elements[0].elements[0].elements

# Modify the create table grammar to include ICEBERG
create_grammar_first_part_new = Sequence(
    Ref("CreateKeywordSegment"),
    OneOf(
        Sequence(
            IcebergKeywordSegment(),
            Ref("TableKeywordSegment"),
        ),
        Ref("TableKeywordSegment"),
    )
)

# Replace the old grammar with the new one
create_table_segment.match_grammar.elements[0].elements[0].elements = create_grammar_first_part_new.elements

# Add Iceberg properties to table options
table_option_segment = OneOf(
    Sequence(
        CatalogKeywordSegment(),
        Ref("EqualsSegment"),
        Ref("QuotedLiteralSegment"),
    ),
    Sequence(
        ExternalVolumeKeywordSegment(),
        Ref("EqualsSegment"),
        Ref("QuotedLiteralSegment"),
    ),
    Sequence(
        BaseLocationKeywordSegment(),
        Ref("EqualsSegment"),
        Ref("QuotedLiteralSegment"),
    ),
)

table_def = iceberg_dialect.get_segment("TableDefinitionSegment")
table_def.match_grammar = Sequence(
    *table_def.match_grammar.elements,
    # Add optional Iceberg properties
    OneOf(
        table_option_segment,
        optional=True
    ),
    OneOf(
        table_option_segment,
        optional=True
    ),
    OneOf(
        table_option_segment,
        optional=True
    ),
)

# Replace the dialect
iceberg_dialect.replace()
