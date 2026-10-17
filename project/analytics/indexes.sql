CREATE INDEX visit_member_visited_idx ON visit (member_id, visited_at);
CREATE INDEX visit_booked_partial_idx ON visit (visited_at) WHERE state = 'booked';