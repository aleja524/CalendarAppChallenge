from dataclasses import dataclass, field
from datetime import datetime, date, time
from email.policy import EmailPolicy
from typing import ClassVar, Dict, Optional

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_err


# TODO: Implement Reminder class here
@dataclass
class Reminder:
    EMAIL: ClassVar[str] = "email"
    SYSTEM: ClassVar[str] = "system"

    date_time: datetime
    type: str = EMAIL


    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"


# TODO: Implement Event class here
@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time

    reminders: list[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self, date_time: datetime, reminder_type: str):
        reminder = Reminder(date_time=date_time, type=reminder_type)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if 0 <= reminder_index < len(self.reminders):
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self):
        return(
            f"ID: {self.id}\n"
            f"Event title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Time: {self.start_at} - {self.end_at}"
        )

# TODO: Implement Day class here
class Day:

 def __init__(self, date_: date):
    self.date_ = date_
    self.slots: Dict[time, Optional[str]] = {}

# TODO: Implement Calendar class here
