from .. import supabase


def fetch_all_events_by_user(user_id: int):
    return (
        supabase.table(table_name="events")
        .select("*")
        .eq(column="user_id", value=user_id)
        .execute()
    )
