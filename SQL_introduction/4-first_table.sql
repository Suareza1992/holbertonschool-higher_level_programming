-- This script creates a table called first_table in the current database
-- first_table has values: id INT, name VARCHAR(256)
-- If the first_table already exists, no error message will show
CREATE TABLE IF NOT EXISTS first_table(
id INT,
name VARCHAR(256)
);
