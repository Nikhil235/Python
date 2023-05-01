import datetime
import pytz
# Datetime module -> working with dates and times in every application
# how to work with dates, times, datetimes, timedeltas, and timezones


# to declare specific time
d = datetime.date(2023, 4, 23)
# print(d)

# to get a today date
today = datetime.date.today()
# print(today.year)
# print(today.day)

# print(today.weekday())      # Monday-0   Sunday-6
# print(today.isoweekday())  # Monday-1    Sunday-7

# timedeltas -> adding differnce between two dates and time
timedelta = datetime.timedelta(days=7)
# print(today + timedelta)
# print(today - timedelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

# bday = datetime.date(2023, 2, 5)
# till_date = bday - today
# print(till_date.total_seconds())

t = datetime.time(10, 00, 45, 39933)
# print(t)
# print(t.hour)

dt = datetime.datetime(2023, 7, 8, 12, 30, 45, 100000)
# print(dt)
# print(dt.date())
# print(dt.time())

tdelta = datetime.timedelta(hours=7)
# print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()  # Coordinated Universal time (UTC)

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# pytz -> pip install pytz
# The standard library has timezone class for handling arbitrary fixed offsets from UTC and timezone.utc as UTC timezone instance.

dt_1 = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt_1)

# dt_now_1 = datetime.datetime(tz=pytz.UTC)
# print(dt_now_1)

# to view all timezone
# for tz in pytz.all_timezones:
#     # print(tz)

dt_str = "July 26, 2023"

dt_2 = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt_2)

# strftime = Datetime to string
# strptime = string to datetime
