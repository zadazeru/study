# модулі
# print(dir(datetime))
# [
#     "MAXYEAR",
#     "MINYEAR",
#     "__builtins__",
#     "__cached__",
#     "__doc__",
#     "__file__",
#     "__loader__",
#     "__name__",
#     "__package__",
#     "__spec__",
#     "date",
#     "datetime",
#     "datetime_CAPI",
#     "sys",
#     "time",
#     "timedelta",
#     "timezone",
#     "tzinfo",
# ]

# from calendar import month
from datetime import date, time
from hmac import new
# import time

# # Отримання інформації про дату та час
# now = datetime.now()
# print(now)
# day = now.day
# month = now.month
# year = now.year  # 2021
# hour = now.hour  # 7
# minute = now.minute  # 38
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, minute, second, timestamp)
# print("timestamp", timestamp)
# print(
#     f"На даний момент {month} місяць грудень ,{day} грудня був дуже холодним . Скоро закінчиться {year} рік"
# )


# Форматування виводу дати за допомогою strftime

# new_year = datetime(2025, 12, 15)
# print(new_year)
# day = new_year.day
# month = new_year.month
# year = new_year.year
# hour = new_year.hour
# minute = new_year.minute
# second = new_year.second
# print(day, month, year, hour, minute, second)

# now = datetime.now()
# t = now.strftime("%H:%M:S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("time one", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# print("time two", time_two)

# Використання дати з datetime
# d = date(2025, 12, 15)
# print(d)
# print("Current day:", d.today())
# today = date.today()
# print("Current year:", today.year)  # 2019
# print("Current month:", today.month)  # 12
# print("Current day:", today.day)

# Об'єкти часу для представлення часу

a = time()
print("a=", a)
b = time(10, 30, 50)
print("b = ", b)
c = time(hour=10, minute=30, second=50)
print("c=", c)
d = time(10, 30, 50, 2099)
print("d=", d)

# Різниця між двома моментами часу за допомогою
today = date(year=2025, month=12, day=16)
new_year = date(year=2026, month=1, day=1)
time_left_for_new_year = new_year - today
print(time_left_for_new_year)
