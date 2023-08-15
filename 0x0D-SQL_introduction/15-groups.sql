-- display the number of records with same score
-- show score and number only
SELECT score, COUNT(*) number FROM second_table
GROUP BY score ORDER BY number DESC;
