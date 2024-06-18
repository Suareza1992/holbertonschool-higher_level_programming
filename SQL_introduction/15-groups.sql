-- This script lists the number of records with the same score in second_table
-- Displays score, number of records for that score labeled number
-- Sorted by descending number of records
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
