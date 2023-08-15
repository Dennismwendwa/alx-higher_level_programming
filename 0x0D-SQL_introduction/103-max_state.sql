-- prints max tempareture of each city
SELECT state, MAXT(value) AS max_temp FROM temperatures GROUP BY state
ORDER BY state;
