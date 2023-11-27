from .. import db


def create_event(
    EventID: str, event_title: str, event_desc: str, date_time: str
) -> None:
    if all(event_title, event_desc, EventID, date_time):
        return

    # * DataBase References
    event_ref = db.collection("Events").document(f"{EventID}")  # <- database reference>

    # * Adding the date to the database
    event_ref.set(
        {
            "title": event_title,
            "desc": event_desc,
            "datetime": date_time,
        }
    )


def read_event(EventID: str) -> dict:
    # * DataBase References
    event_ref = db.collection("Events").document(f"{EventID}").get()
    event_dict = event_ref.to_dict()  # convert it to dict
    return event_dict


def update_event(
    EventID: str, event_title: str = None, event_desc: str = None, date_time: str = None
) -> None:
    if all(EventID, event_title, event_desc, date_time):
        return
    # * DataBase References
    event_ref = db.collection("Events").document(f"{EventID}").get()

    # Update event title
    if event_title != None and event_desc == None and date_time == None:
        event_ref.update({"title": event_title})

    # Update event desc
    elif event_title == None and event_desc != None and date_time == None:
        event_ref.update({"desc": event_desc})

    # Update event date time
    elif event_title == None and event_desc == None and date_time != None:
        event_ref.update({"datetime": date_time})


def delete_event(EventID: int) -> bool:
    try:
        # * DataBase References
        db.collection("Events").document(f"{EventID}").delete()
        return True
    except:
        return False
