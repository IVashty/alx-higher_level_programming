-- create anew table and give ts values as instructed.
CREATE TABLE IF NOT EXISTS second_table (id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL, score INTEGER NOT NULL);
INSERT IGNORE INTO second_table (id,name,score) VALUES (1, 'John',10);
INSERT IGNORE INTO second_table (id,name,score) VALUES (2, 'Alex',3);
INSERT IGNORE INTO second_table (id,name,score) VALUES (3, 'Bob',14);
INSERT IGNORE INTO second_table (id,name,score) VALUES (4, 'George',8);
