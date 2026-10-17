VARIANT = 15


def indexes() -> list[str]:
    return [
        "CREATE INDEX visit_member_state_visited_idx ON visit (member_id, state, visited_at)"
    ]