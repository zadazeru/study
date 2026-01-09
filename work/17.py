# def num_list(a, b, c, d, i, j):
#     return a + b + c + d + i + j
# lst = [3, 54, 545, 354, 34, 90]
# print(num_list(*lst))


# num = range(5, 100)
# print(list(num))
# arg = [3, 78, 45]
# numbers = range(*arg)
# print(numbers)


# countries = ["Finlandia", "Sweden", "norway", "Denvark", "Iceland"]
# fin, sw, nor, den, *ice = countries
# print(fin, sw, nor, den, ice)

# Розпакування словників


# def unpacking_lst(name, countries, city, age):
#     return f"{name} live in {countries}, {city}. She is {age} years old "


# dct = {"name": "Alisabet", "countries": "Moldova", "city": "Bucharest", "age": "25"}
# print(unpacking_lst(**dct))


# Пакувальні списки
# def all_sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(all_sum(1, 3, 5))
# print(all_sum(5, 3, 6))
# def packing_personal_info(**kwards):
#     for key in kwards:
#         print(f"{key} = {kwards[key]}")
#     return kwards


# print(packing_personal_info(name="adsd", counrty="fin", city="ds", age=23))
