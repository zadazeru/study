# Завдання №4,5,6
# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
# names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for country in countries:
#     print(country)
# for name in names:
#     print(name)
# for num in numbers:
#     print(num)


# Завдання №6,7,8


# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
# names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# countries_upper = list(map(lambda a: a.upper(), countries))
# print(countries_upper)

# num_square = list(map(lambda a: a**2, numbers))
# print(num_square)

# names_big = list(map(lambda a: a.upper(), names))
# print(names_big)


# Завдання №10,11,12,13

# countries_land = list(filter(lambda a: "land" in a, countries))
# print(countries_land)

# six_countries_letter = list(filter(lambda a: len(a) == 7, countries))
# print(six_countries_letter)

# six_countries_letter_more_big = list(filter(lambda a: len(a) >= 6, countries))
# print(six_countries_letter_more_big)

# e_countries = list(filter(lambda a: a.startswith("E"), countries))
# print(e_countries)


# Завдання №14
# chain_countries = list(
#     map(lambda a: a.upper(), filter(lambda b: b.startswith("F"), countries))
# )
# print(chain_countries)


# # Завдання №15
# def get_string_lists(input_list):
#     return list(filter(lambda item: isinstance(item, str), input_list))


# mixed_data = [1, 2, "Python", "lisy", "Code", 56]
# print(get_string_lists(mixed_data))

# Завдання №15

# from functools import reduce


# total_sum = reduce(lambda a, b: a + b, numbers)
# print(total_sum)

# total_list_of_countries = reduce(
#     lambda acc, curr: f"{acc},{curr}", countries
# )  # acc - це накопичений рядок, curr - поточна країна
# print(total_list_of_countries)

# sentences = f"{total_list_of_countries} are north countries"
# print(sentences)


def categorize_countries(filename):
    with open(filename) as f:
        countries = [line.strip() for line in f]
    return list(filter(lambda a: "stan" in a, countries))


print(categorize_countries(r"C:\Users\Admin\Documents\study\.github\dz\countries.txt"))


def count_countries_by_start_letter(filename):
    counts = {}  # Створюємо пустий словник

    # Читаємо країни з файлу
    with open(filename) as f:
        countries = [line.strip() for line in f]

    for country in countries:
        first_letter = country[0]  # Беремо першу букву

        # Якщо така буква вже є в ключах - збільшуємо лічильник
        if first_letter in counts:
            counts[first_letter] += 1
        # Якщо немає - створюємо запис = 1
        else:
            counts[first_letter] = 1

    return counts


# Перевірка
print(
    "Статистика по буквах:",
    count_countries_by_start_letter(
        r"C:\Users\Admin\Documents\study\.github\dz\countries.txt"
    ),
)
