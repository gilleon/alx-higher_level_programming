-- import dump into hbtn_0c_0
-- displays avg temp and group by city
SELECT city, AVG(value) avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;