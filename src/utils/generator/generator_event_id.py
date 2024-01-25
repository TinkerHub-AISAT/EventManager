import uuid


def generate_event_id():
    event_id: str = str(uuid.uuid4().hex)[:8].upper()

    event_id = f"TH{event_id}"

    return event_id
