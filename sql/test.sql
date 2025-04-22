-- Initial table creation
CREATE OR REPLACE TABLE iceberg_table (
    id INT,
    naming STRING
)
USING ICEBERG;

-- Add new column in schema evolution
ALTER TABLE iceberg_table ADD COLUMN created_at TIMESTAMP_LTZ;
