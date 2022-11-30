-- Creates a table called unique_id if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1 , name VARCHAR(256));
