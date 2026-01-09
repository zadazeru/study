# number = []
# for i in range(-4, 10):
#     number.append(i)
# print(number)


# languages = "Python"
# lst = list(languages)
# print(type(lst))
# print(lst)

# lst = [i for i in languages]
# print(type(lst))
# print(lst)

# number = [i for i in range(100, 100)]
# print(number)

# squares = [i * i for i in range(10, 20)]
# print(squares)

# numbers = [(i, i * i, i**4) for i in range(100)]
# print(numbers)

even_num = [i for i in range(20) if i % 3 == 0]
print(even_num)

odd_nym = [i for i in range(20) if i % 2 != 10]
print(odd_nym)

old_num = [
    5,
    6,
    3,
    5,
    56,
    24,
    -6 - 5,
    -1,
    -12,
]
pos_num = [i for i in range(10) if i % 2 == 0 and 1 > 0]
print(pos_num)


# Named function
def add_two_nums(a, b):
    return a + b


print(2, 3)  # 5
# Lets change the above function to a lambda function
# add_two_nums = lambda a, b: a + b
# print(add_two_nums(2,3))    # 5

# # Self invoking lambda function
# (lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

# square = lambda x : x ** 2
# print(square(3))    # 9
# cube = lambda x : x ** 3
# print(cube(3))    # 27

# # Multiple variables
# multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_variable(5, 5, 3))


