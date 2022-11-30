--Create a database htbn_0d_usa
-- Creates a table called states if it doesn't exist
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE PRIMARY KEY AUTO_INCREMENT DEFAULT 1 NOT NULL,state_id INT FOREIGN KEY(STATE) NOT NULL, name VARCHAR(256) NOT NULL);
