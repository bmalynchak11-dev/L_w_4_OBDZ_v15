-- title: Середня оплата за статусами відвідувань
SELECT state, COUNT(*) AS count_records, ROUND(AVG(paid), 2) AS avg_paid
FROM visit
GROUP BY state
ORDER BY count_records DESC;