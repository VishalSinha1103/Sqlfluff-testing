-- Create users table
CREATE TABLE users (
    id INT PRIMARY KEY,
    "name" VARCHAR(100),         -- Escaped to avoid reserved keyword issue
    "email" VARCHAR(100),        -- Escaped to avoid reserved keyword issue
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (id, "name", "email") VALUES
(1, 'Alice', 'alice@example.com'),
(2, 'Bob', 'bob@example.com');

-- Environment-specific condition (proper formatting)
SELECT
    id,
    "name",
    "email",
    created_at
FROM users
WHERE "env" = '@dev@';           -- Proper line formatting
