from setuptools import setup, find_packages

setup(
    name="sqlfluff-plugin-iceberg",
    version="0.1.0",
    description="SQLFluff plugin for Iceberg SQL",
    packages=find_packages(),
    entry_points={
        "sqlfluff": [
            "sqlfluff_plugin_iceberg=sqlfluff_plugin_iceberg",
        ]
    },
    install_requires=["sqlfluff>=3.4.0"],
)
