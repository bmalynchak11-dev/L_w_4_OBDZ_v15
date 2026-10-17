SELECT setval(pg_get_serial_sequence('trainer', 'id'), COALESCE(MAX(id), 1)) FROM trainer;
SELECT setval(pg_get_serial_sequence('workout_room', 'id'), COALESCE(MAX(id), 1)) FROM workout_room;
SELECT setval(pg_get_serial_sequence('membership_plan', 'id'), COALESCE(MAX(id), 1)) FROM membership_plan;
SELECT setval(pg_get_serial_sequence('member', 'id'), COALESCE(MAX(id), 1)) FROM member;
SELECT setval(pg_get_serial_sequence('workout', 'id'), COALESCE(MAX(id), 1)) FROM workout;
SELECT setval(pg_get_serial_sequence('visit', 'id'), COALESCE(MAX(id), 1)) FROM visit;