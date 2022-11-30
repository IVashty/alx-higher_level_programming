--Create a database htbn_0d_usa
-- Creates a table called states if it doesn't exist
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
USE htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE PRIMARY KEY AUTO_INCREMENT , name VARCHAR(256));
