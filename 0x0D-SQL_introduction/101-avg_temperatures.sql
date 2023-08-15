-- prints tenpreture average
SELECT city, AVG(valu) as avg_temp
FROM temperature GROUP BY city
ORDER BY avg_temp DESC;
