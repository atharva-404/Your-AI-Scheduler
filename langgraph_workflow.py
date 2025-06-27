import dateparser
from calendar_service import get_free_slots, book_event,get_user_calendar_id
from datetime import timedelta
import dateparser
from datetime import datetime
import parsedatetime
from datetime import datetime

def parse_datetime(user_input):
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse(user_input)

    if parse_status == 0:
        print("Could not parse date/time.")
        return None

    dt = datetime(*time_struct[:6])
    print("Parsed datetime:", dt)
    return dt

def process_message(user_input):
    get_user_calendar_id()
    dt = parse_datetime(user_input)
    print(dt)
    if not dt:
        return "Sorry, I couldn't understand the date or time. Please try again with more clarity."

    if "free time" in user_input or "available" in user_input:
        free_slots = get_free_slots(dt.date())
        if free_slots:
            slot_strings = [f"{s.strftime('%I:%M %p')} to {e.strftime('%I:%M %p')}" for s, e in free_slots]
            return "You're free at: " + ", ".join(slot_strings)
        else:
            return "You don't seem to have any free time on that day."

    elif "between" in user_input:
        words = user_input.split("between")
        time_range = words[1] if len(words) > 1 else ""
        start_end = time_range.strip().split("and") if "and" in time_range else time_range.strip().split("-")
        if len(start_end) == 2:
            start_time = dateparser.parse(start_end[0], settings={'RELATIVE_BASE': dt})
            end_time = dateparser.parse(start_end[1], settings={'RELATIVE_BASE': dt})
            if start_time and end_time:
                free_slots = get_free_slots(dt.date())
                for start, end in free_slots:
                    if start_time.time() <= start.time() <= end_time.time():
                        book_event("Meeting via TailorTalk", start)
                        return f"Booked a meeting from {start.strftime('%I:%M %p')} on {start.strftime('%A, %B %d')}."
                return "No free slots in that time range."
        return "Sorry, couldn't parse your requested time range."

    else:
        success = book_event("Meeting via TailorTalk", dt)
        if success:
            return f"You're booked for {dt.strftime('%A, %B %d at %I:%M %p')}."
        else:
            return "Sorry, that time is not available or booking failed."
