--Create a database htbn_0d_usa
-- Creates a table called states if it doesn't exist
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
