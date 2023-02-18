-- lists all records of the table with 'name' values
-- 'second_table' of the database in MySQL server

SELECT score,
       name
  FROM second_table
 WHERE name IS NOT NULL
 ORDER BY score DESC;
