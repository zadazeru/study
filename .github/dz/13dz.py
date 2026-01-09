# number = []
# for i in range(-4, 10):
#     number.append(i)
# print(number)

# list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattend = []
# for i in list_of_lists:
#     for j in i:
#         for k in j:
#             flattend.append(k)
# print(flattend)


# result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
# print(result)

# №5
# countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
# result = [
#     item.upper()
#     for country_list in countries
#     for country_tuple in country_list
#     for item in country_tuple
# ]
# print(result)

# №6
# def main_name(first_name, last_name):
#     return f"{first_name} {last_name}"


# names = [
#     [("Asabeneh", "Yetaeyeh")],
#     [("David", "Smith")],
#     [("Donald", "Trump")],
#     [("Bill", "Gates")],
# ]
# result = []
# for name_list in names:
#     for name_tuple in name_list:
#         first_name, last_name = name_tuple
#         result.append(main_name(first_name, last_name))
# print(result)

# №7
# Lambda function to calculate slope given two points
# def slope(x1, y1, x2, y2):
#     return (y2 - y1) / (x2 - x1)


# # Lambda function to calculate y-intercept
# def y_intercept(m, x, y):
#     return y - m * x


# # Example: Two points (1, 2) and (3, 6)
# m = slope(1, 2, 3, 6)
# b = y_intercept(m, 1, 2)

# print(f"Нахил: {m}")
# print(f"Y-перетин: {b}")
# print(f"Рівняння: y = {m}x + {b}")


# inventar = {"gold": 50, "sword": "woden", "potion": 2}
# print(f"У тебе {inventar ['gold']} золота")

# print("О ні !Гоблін вкрав мій меч..")
# inventar["sword"] = "None"
# print("Ти знайшла скриню")
# inventar["gold"] = inventar["gold"] + 100
# inventar["shield"] = "iron"
# print("\nОсь твій інвентар")
# print(inventar)


# hero = {
#     "name": "Oleg",
#     "hp": 100,
#     "inventory": {"gold": 50, "item": ["apple", "potion"]},
# }
# hero["inventory"]["item"].remove("apple")
# hero["hp"] = hero["hp"] + 10

# hero["inventory"]["item"].append("sword")
# hero["inventory"]["gold"] += 100
# print(hero)


import json
import urllib.request


def get_weather_kyiv():
    # Це адреса сервера погоди (координати Києва)
    url = "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=true"

    # Відкриваємо інтернет-з'єднання
    response = urllib.request.urlopen(url)

    # Читаємо дані та перетворюємо їх у Словник Python
    data = json.loads(response.read())

    # Повертаємо тільки шматочок з поточною погодою
    return data["current_weather"]


def suggest_clothes(temp):
    # Виправлена логіка порівняння:

    if temp < 0:
        return "Вдягай пуховик і шапку ❄️"

    # "Якщо температура від 0 до 10 включно"
    elif 0 <= temp <= 10:
        return "Пальто або тепла куртка підійде 🧥"

    # "Якщо температура від 11 до 20 включно"
    elif 11 <= temp <= 20:
        return "Можна в худі або легкій куртці 🍃"

    # В усіх інших випадках (значить більше 20)
    else:
        return "Футболка і шорти ☀️"


print("Зв'язуюсь із супутником... 📡")

print("Зв'язуюсь із спутником...")
weather_data = get_weather_kyiv()
current_temp = weather_data["temperature"]
print(f"Зараз {current_temp} градусів у Києві")
advice = suggest_clothes(current_temp)
print(f"Порада: {advice}")
