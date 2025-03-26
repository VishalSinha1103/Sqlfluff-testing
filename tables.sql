-- Create users table
CREATE TABLE users (
    id INT PRIMARY KEY,
    "name" VARCHAR(100),
    "email" VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (id, name, email) VALUES
(1, 'Alice', 'alice@example.com'),
(2, 'Bob', 'bob@example.com');

-- Environment-specific condition (improved formatting)
SELECT *
FROM users
WHERE "env" = '@dev@';  -- Use quotes to avoid reserved keyword issue
