-- This script lists all records of the table second_table
-- Doesn't list rows without a name value
-- Displays score & name in descending score order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER by score DESC;
