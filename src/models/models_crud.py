from .. import supabase


def event_fetch_all():
    return supabase.table(table_name="events").select("*").execute()


def event_fetch_by_id(event_id: str):
    return (
        supabase.table(table_name="events")
        .select("*")
        .eq(column="event_id", value=event_id)
        .execute()
    )


def event_update(event_id: str, data: dict):
    return (
        supabase.table(table_name="events")
        .update(json=data)
        .eq(column="event_id", value=event_id)
        .execute()
    )


def event_delete(event_id: str):
    return (
        supabase.table(table_name="events")
        .delete()
        .eq(column="event_id", value=event_id)
        .execute()
    )
