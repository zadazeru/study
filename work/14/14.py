# def square(x):
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)

# # Convert the map object to a list
# squared_numbers_list = list(squared_numbers)
# print(squared_numbers_list)


# try:
#     with open("21-4.txt") as f:
#         n = int(f.readline())
#         for i in range(n):
#             a, b = map(int, f.readline().split())
#             print(a + b)
# except FileNotFoundError:
#     print("Error: File '21-4.txt' not found.")
# except ValueError:
#     print("Error: Invalid input format in file.")


# def f(a, b):
#     return a * b
# a = map(f, [1, 2, 3, 5, 5, 6], [6, 8, 6, 5, 4, 8])
# print(list(a))


# def f(a, b):
#     return a * b
# a = map(lambda x: x + 15, (2, 7, 6, 4))
# print(list(a))


# def f(a):
#     if a % 2 == 0:
#         return a


# a = filter(lambda x: (x % 2 == 0), (2, 7, 6, 4))
# print(list(a))

# from functools import reduce

# print(reduce(lambda a, b: a * b, (50, 78, 34, 23, 78)))

# from unittest import result


# a = [1, 4, 6, 7]
# b = "asdo"
# result = zip(a, b)
# print(list(result))

# Синтаксис:
# with open("ім'я_файлу", "режим", кодування) as прізвисько:

with open("shodennyk.txt", "w", encoding="utf-8") as file:
    file.write("Привіт! Це мій перший запис.")
