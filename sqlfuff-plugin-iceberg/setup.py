from setuptools import setup, find_packages

setup(
    name='sqlfluff-plugin-iceberg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sqlfluff',  # Any other dependencies your plugin may have
    ],
)
