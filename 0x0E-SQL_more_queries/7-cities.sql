-- create a database htbn_0d_usa and creates a table called states if it doesn't EXISTS
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
USE htbn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
        id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
        state_id INT NOT NULL,
        FOREIGN KEY(state_id) REFERENCES states(id),
        name VARCHAR(256) NOT NULL
);
