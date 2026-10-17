SELECT setval(pg_get_serial_sequence('project.member', 'id'), COALESCE(MAX(id), 1), true) FROM member;
SELECT setval(pg_get_serial_sequence('project.workout', 'id'), COALESCE(MAX(id), 1), true) FROM workout;
SELECT setval(pg_get_serial_sequence('project.visit', 'id'), COALESCE(MAX(id), 1), true) FROM visit;