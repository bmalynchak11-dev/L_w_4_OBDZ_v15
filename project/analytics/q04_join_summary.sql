-- title: Зведення відвідувань за видами тренувань
SELECT w.title, COUNT(v.id) AS total_visits, SUM(v.paid) AS total_revenue
FROM visit v
JOIN workout w ON v.workout_id = w.id
GROUP BY w.id, w.title
ORDER BY total_revenue DESC, w.id;