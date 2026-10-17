-- title: Вибірка відвідувань конкретного клієнта з назвами тренувань
SELECT v.id, w.title, v.paid, v.visited_at
FROM visit v
JOIN workout w ON v.workout_id = w.id
WHERE v.member_id = 42 AND v.visited_at >= '2024-06-01'
ORDER BY v.visited_at, v.id;