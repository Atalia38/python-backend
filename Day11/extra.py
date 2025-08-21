import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))

print(validate_email("atalia_123@example-domain.com")) 
print(validate_email("atalia_123@example-")) 






def extract_dates(text):
    pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4})\b'
    return re.findall(pattern, text)


text = "We met on 12-08-2023 and again on 25/12/2023."
print(extract_dates(text))  




from datetime import datetime, timedelta

def time_until_next_birthday(birthday_str):
    today = datetime.today()
    birthdate = datetime.strptime(birthday_str, "%Y-%m-%d")
    next_birthday = birthdate.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return days, hours, minutes

print(time_until_next_birthday("1995-10-01")) 



from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):
    fmt = "%Y-%m-%d %H:%M:%S"
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    dt = datetime.strptime(time_str, fmt)
    dt = from_zone.localize(dt)
    converted = dt.astimezone(to_zone)
    return converted.strftime(fmt)


print(convert_timezone("2023-10-05 14:30:00", "US/Eastern", "UTC"))




def parse_log_timestamps(log):
    pattern = r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) \+\d{4}\]'
    month_map = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
                    'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

    results = []
    for match in re.findall(pattern, log):
        day, mon, year, hour, minute, second = match
        dt = datetime(int(year), month_map[mon], int(day), int(hour), int(minute), int(second))
        dt_utc = dt.strftime('%Y-%m-%d %H:%M:%S')
        results.append(dt_utc)

    return results


log = "[21/Aug/2025:12:34:56 +0000] some event [22/Aug/2025:01:00:00 +0000]"
print(parse_log_timestamps(log))




