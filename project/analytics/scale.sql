-- Масштабування таблиці до 100 000+ рядків
INSERT INTO visit (id, member_id, workout_id, places, paid, state, visited_at, comment)
OVERRIDING SYSTEM VALUE
SELECT 
    g AS id,
    ((g * 17) % 1000) + 1 AS member_id,
    ((g * 31) % 50) + 1 AS workout_id,
    (g % 4) + 1 AS places,
    ((g % 500) + 50)::numeric(12,2) AS paid,
    CASE 
        WHEN g % 100 = 0 THEN 'booked'
        WHEN g % 20 = 0 THEN 'missed'
        ELSE 'attended'
    END AS state,
    TIMESTAMP '2024-01-01 08:00:00' + ((g % 500) || ' days')::interval + ((g % 86400) || ' seconds')::interval AS visited_at,
    'Auto generated visit note ' || md5(g::text) AS comment
FROM generate_series(1, 110000) AS g
ON CONFLICT (id) DO NOTHING;