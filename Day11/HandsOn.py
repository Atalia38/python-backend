import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

emails = ["test@example.com", "invalid@com", "user.name@domain.co"]
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")






    from datetime import datetime, timedelta

now = datetime.now()
print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


future_date = now + timedelta(days=5)
print("5 Days Later:", future_date.strftime("%Y-%m-%d"))




from datetime import datetime
import pytz

def display_time_in_timezones(timezones):
    utc_now = datetime.now(pytz.utc)
    for tz in timezones:
        tz_time = utc_now.astimezone(pytz.timezone(tz))
        print(f"{tz}: {tz_time.strftime('%Y-%m-%d %H:%M:%S')}")


zones = ['Asia/Kolkata', 'America/New_York', 'Europe/London']
display_time_in_timezones(zones)




