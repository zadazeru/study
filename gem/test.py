# print("Створюємо файл...")
# with open("test_file.txt", "w", encoding="utf-8") as f:
#     f.write("Рядок 1: Це початок .\n")

# print("Дописуємо дані...")
# with open("test_file.txt", "a", encoding="utf-8") as f:
#     f.write("Рядок 2: Це я дописала пізніше\n")

# print("Читаю файл...")
# with open("test_file.txt", "r", encoding="utf-8") as f:
#     content = f.read
#     print(content)
import os

print("Мій особистий щоденник")
print("Пиши і натискай Enter")

while True:
    text = input("Твій запис:")

    if text == "read":
        print("\nВідкриваю сторінку")
        try:
            with open("diary.txt", "r", encoding="utf-8") as file:
                content = file.read
                print("-" * 20)
                print(content)
                print("-" * 20)
        except FileNotFoundError:
            print("Щоденник ще пустий. Напиши щось ")
