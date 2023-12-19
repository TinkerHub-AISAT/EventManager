from .. import supabase


def event_fetch_all():
    """Returns all the events
    Returns:
        `APIResponse`
    """
    return supabase.table(table_name="events").select("*").execute()


def event_fetch_by_id(event_id: str):
    """fetchs the data by event ID

    Args:
        `event_id (str)`: Events ID

    Returns:
        `APIResponse`
    """
    return (
        supabase.table(table_name="events")
        .select("*")
        .eq(column="event_id", value=event_id)
        .execute()
    )


def event_update(event_id: str, data: dict):
    """updates the event data

    Args:
        `event_id (str)`: Event ID
        `data (dict)`: dict with event data (Title, desc)

    Returns:
        `APIResponse`
    """
    return (
        supabase.table(table_name="events")
        .update(json=data)
        .eq(column="event_id", value=event_id)
        .execute()
    )


def event_delete(event_id: str):
    """delete the event data by event ID

    Args:
        `event_id (str)`: Events ID

    Returns:
        `APIResponse`
    """
    return (
        supabase.table(table_name="events")
        .delete()
        .eq(column="event_id", value=event_id)
        .execute()
    )


def event_create(event_data: dict):
    """Creates a new event

    Args:
        `event_data (dict)`: dictionary

    Returns:
        `APIResponse`
    """
    return supabase.table(table_name="events").insert(json=event_data).execute()
