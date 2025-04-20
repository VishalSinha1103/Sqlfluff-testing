from sqlfluff.core.parser import (
    BaseSegment,
    KeywordSegment,
    StringParser,
)

class CreateIcebergTableSegment(BaseSegment):
    """This represents the CREATE ICEBERG TABLE statement."""
    
    type = "create_iceberg_table"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name")
    
    @classmethod
    def parse(cls, *args, **kwargs):
        # Simple parsing to match the "CREATE ICEBERG TABLE" statement
        return cls.parse_segment(
            KeywordSegment("CREATE"),
            KeywordSegment("ICEBERG"),
            KeywordSegment("TABLE"),
            StringParser("name"),
        )


def create_iceberg_table_segment():
    return CreateIcebergTableSegment
