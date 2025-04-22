from setuptools import setup, find_packages

setup(
    name="sqlfluff-plugin-iceberg",
    version="0.1.0",
    description="SQLFluff plugin for Snowflake CREATE ICEBERG TABLE support",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "sqlfluff>=2.0.0",
    ],
    entry_points={
        "sqlfluff": [
            "sqlfluff_snowflake_iceberg=sqlfluff_plugin_iceberg",
        ],
    },
    python_requires=">=3.7",
)
