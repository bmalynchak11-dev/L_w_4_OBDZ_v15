-- title: Список майбутніх відкритих бронювань
SELECT id, member_id, visited_at
FROM visit
WHERE state = 'booked' AND visited_at >= '2024-09-01'
ORDER BY visited_at, id;