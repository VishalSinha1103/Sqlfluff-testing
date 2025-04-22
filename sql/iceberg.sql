CREATE ICEBERG TABLE IF NOT EXISTS testin (
    id INT PRIMARY KEY,
    "name" VARCHAR(100),         -- Escaped to avoid reserved keyword issue
    "email" VARCHAR(100),        -- Escaped to avoid reserved keyword issue
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
