# №1
import random
# import string


# def random_user_id():
#     cha_source = string.ascii_letters + string.digits
#     result = ""
#     for i in range(6):
#         result += random.choice(cha_source)
#     return result


# print(random_user_id())


# # №2
# def user_id_gen_by_user():
#     print("Введіть параметри генерації:")
#     char_count = int(input("ID lenght"))
#     id_count = int(input("ID count"))

#     char_source = string.ascii_letters + string.digits

#     for i in range(id_count):
#         result = ""
#         for j in range(char_count):
#             result += random.choice(char_source)
#     print(result)


# user_id_gen_by_user()


# №3
# def rgb_color_gen():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return f"rgb({r},{g},{b})"


# print(rgb_color_gen())
# №4
# def list_of_hexa_colors(how_many):
#     results = []
#     hex_chars = "0123456789ABCDEF"
#     for i in range(how_many):
#         color = "#"
#         for j in range(6):
#             color += random.choice(hex_chars)
#             color = color.upper()
#         results.append(color)
#     return results
# print(list_of_hexa_colors(7))
# №5
# def list_of_rgb_colors(count):
#     my_color_list = []
#     for i in range(count):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         color_string = f"rgb({r},{g},{b})"
#         my_color_list.append(color_string)
#     return my_color_list
# print(list_of_rgb_colors(10))
# №6


def generate_colors(mode, count):
    results = []  # Загальний список для результату

    # Сценарій 1: Якщо просять HEXA
    if mode == "hexa":
        chars = "0123456789abcdef"
        for i in range(count):
            color = "#"
            for j in range(6):
                color += random.choice(chars)
            results.append(color)

    # Сценарій 2: Якщо просять RGB
    elif mode == "rgb":
        for i in range(count):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f"rgb({r},{g},{b})"
            results.append(color)

    # Повернення результату (один раз на самому кінці!)
    return results


# Тестуємо різні варіанти:
print("Hexa (3):", generate_colors("hexa", 3))
print("Hexa (1):", generate_colors("hexa", 1))
print("RGB (3): ", generate_colors("rgb", 3))
print("RGB (1): ", generate_colors("rgb", 1))  # ['rgb(33,79, 176)']
