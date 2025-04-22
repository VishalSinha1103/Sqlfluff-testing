from setuptools import setup, find_packages

setup(
    name="sqlfluff-snowflake-iceberg",
    version="0.1.0",
    description="SQLFluff plugin for Snowflake CREATE ICEBERG TABLE support",
    author="Your Name",
    author_email="your.email@example.com",
    packages=["sqlfluff_snowflake_iceberg"],  # Be explicit about packages
    install_requires=[
        "sqlfluff>=2.0.0,<4.0.0",  # Support SQLFluff 2.x and 3.x
    ],
    entry_points={
        "sqlfluff": [
            "sqlfluff_snowflake_iceberg=sqlfluff_snowflake_iceberg",
        ],
    },
    python_requires=">=3.7",
)
