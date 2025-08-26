import re
from datetime import datetime
import pytz

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def display_time_in_timezones(timezones):
    utc_now = datetime.now(pytz.utc)
    for tz in timezones:
        tz_time = utc_now.astimezone(pytz.timezone(tz))
        print(f"{tz}: {tz_time.strftime('%Y-%m-%d %H:%M:%S')}")


email = input("Enter your email: ")

if is_valid_email(email):
    print("Email is valid.")
    print("Current time in different timezones:")
    display_time_in_timezones(['Asia/Kolkata', 'America/New_York', 'Europe/London'])
else:
    print("Invalid email format.")

