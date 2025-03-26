-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10, 2),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample orders
INSERT INTO orders (order_id, user_id, amount, status) VALUES
(101, 1, 250.00, 'pending'),
(102, 2, 400.50, 'completed');

-- Environment-specific filter
SELECT * FROM orders WHERE status = '@test@';

