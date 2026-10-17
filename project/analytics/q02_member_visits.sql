-- title: Вибірка відвідувань конкретного клієнта за період
SELECT id, workout_id, paid, visited_at
FROM visit
WHERE member_id = 42 AND visited_at >= '2024-06-01'
ORDER BY visited_at, id;