# №1
from calendar import month
from datetime import datetime, time

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
second = now.second
print("Поточний час", day, month, year, hour, second)

now_time = now.strftime("%m.%d.%Y")
or_time = now.strftime("%H/%M/%S")
print(now_time)

print(f"Сьогодні {now_time} або {or_time}")


# Різниця між двома моментами часу за допомогою
today = datetime(year=2025, month=12, day=16)
new_year = datetime(year=2026, month=1, day=1)
time_left_for_new_year = new_year - today
print(time_left_for_new_year)
