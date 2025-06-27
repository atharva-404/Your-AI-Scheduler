from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta, datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)

def get_free_slots(date, duration_minutes=30):
    service = get_calendar_service()
    start_of_day = datetime.combine(date, datetime.min.time())
    end_of_day = start_of_day + timedelta(days=1)

    events_result = service.events().list(calendarId='primary',
                                          timeMin=start_of_day.isoformat() + 'Z',
                                          timeMax=end_of_day.isoformat() + 'Z',
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    busy_times = [(datetime.fromisoformat(e['start']['dateTime'].replace('Z', '')), 
                   datetime.fromisoformat(e['end']['dateTime'].replace('Z', ''))) for e in events if 'dateTime' in e['start']]

    free_slots = []
    current = start_of_day
    while current + timedelta(minutes=duration_minutes) <= end_of_day:
        next_slot = current + timedelta(minutes=duration_minutes)
        overlap = any(start < next_slot and current < end for start, end in busy_times)
        if not overlap:
            free_slots.append((current, next_slot))
        current = next_slot
    return free_slots

def book_event(summary, start_dt, duration_minutes=30):
    service = get_calendar_service()
    calendar_id = 'atharvasonar32@gmail.com'

    end_dt = start_dt + timedelta(minutes=duration_minutes)
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }
    try:
        service.events().insert(calendarId=calendar_id, body=event).execute()
        return True
    except Exception as e:
        print("Booking error:", e)
        return False

def get_user_calendar_id():
    service = get_calendar_service()
    calendar_list = service.calendarList().list().execute()
    for calendar in calendar_list.get('items', []):
        print(calendar['id'])
