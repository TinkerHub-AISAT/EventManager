import uuid


def generate_event_id():
    # Use UUID to generate a unique identifier
    event_id = str(uuid.uuid4().hex)[:8].upper()

    event_id = f"TH{event_id}"

    return event_id
