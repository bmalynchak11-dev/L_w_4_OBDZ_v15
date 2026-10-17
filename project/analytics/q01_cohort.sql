-- title: Перший візит клієнтів за місяцями (когорти)
WITH first_visits AS (
    SELECT member_id, date_trunc('month', MIN(visited_at)) AS cohort_month
    FROM visit
    GROUP BY member_id
)
SELECT cohort_month, COUNT(*) AS new_members
FROM first_visits
GROUP BY cohort_month
ORDER BY cohort_month;