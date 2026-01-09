# N = 5
# for i in range(N):
#     for j in range(5 * 5):
#         print("x", end="")
#     print()

# number = range(1,10)
# for inter in range ():
#     print(number)
# else:
#     print(number)

# for number in range(15):
#     print(number, 'x', number, '=', number * number)

# lang = {

#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],

#     }

# for key in lang:
#     if key == 'skills':
#         for skill in lang['skills']:
#             print(skill)

# for i in range(0,100,2):
#     print(i)

# for i in range(1,100,2):
#     print(i)

# total = sum(range(101))
# print("The sum of all numbers is",total)

# total = sum(range(0,100,2))
# total1= sum(range(1,100,2))
# print( "the sum of all evens is",total)
# print("the sum of all evens and the sum of all ",total1)


# fruit=['banana', 'orange', 'mango', 'lemon']
# print(list(reversed(fruit)))

# shuruna_room = input("Введіть ширину кімнати:")
# cost_laminat = input("Введіть вартість ламінату за м2:")
# dovchuna_room = input("Введіть довжину кімнати:")
# ploshad = float(shuruna_room) * float(dovchuna_room)
# print(float(cost_laminat) * ploshad)
# print("Площа кімнати:", ploshad)

# name = input("Введіть ваше ім'я:")
# place = input("Введіть ваше місто:")
# dieslovo = input("Введіть дію вашого персонажу:")
# food = input("Введіть їжу для споживання:")
# story = f"Одного разу {name} захотів прогулятися по {place}. Під час своєї прогулянки він захотів {dieslovo}. Після цього він зголоднів і з'їв {food}"
# print(story)

# far_tem = float(input("Введіть температуру у фаренгейтах:"))
# celsium = (far_tem - 32) * 5 / 9
# print("Температура у селсіях", celsium)

# color = input("Який колік горить прямо зараз ?(зелений/жовтий/червоний):")
# if color == "червоний":
#     print("Стій ,почекай")
# elif color == "жовтий":
#     print("Почекай ще трохи,скоро буде..")
# elif color == "зелений":
#     print("Можеш сміло йти..")
# else:
#     print("Світлофор зламався ")


# age = int(input("Введіть свій вік: "))
# if age >= 100:
#     print("Вам безкоштовний вхід, шановний!")
# elif age >= 18:
#     print("Вхід дозволено. Гарної вечірки!")
# else:
#     print("Тобі ще рано. Йди додому робити уроки.")

# for i in range(20):
#     print(f"Я обіцяю не захоплювати світ {i}")

# for i in range(5):
#     print("*" * i)


# size = 4

# for i in range(size):  # Зовнішній цикл: відповідає за РЯДКИ (0, 1, 2, 3)
#     for j in range(size):  # Внутрішній цикл: малює СИМВОЛИ в рядку
#         print("#", end=" "  )  # end=" " означає "не переходь на новий рядок, постав пробіл"
#     print()  # Порожній print, щоб натиснути "Enter" в кінці рядка
# start = 6
# stop = 0
# step = -1
# for i in range(start, stop, step):
#     print("#" * i)


# for i in range(6):
#     print(" " * 3 + "*" * i)

# height = 5

# for i in range(1, height + 1):
#     spaces = " " * (height - i)  # Малюємо повітря
#     stars = "*" * i  # Малюємо зірки
#     print(spaces + stars)  # Склеюємо


# stars = 7
# for i in range(stars):
#     print("*" * 2 - i)

# height = 10
# for i in range(1, height + 1):
#     space = " " * (height -i)
#     bricks = "#" * (2 * i - 1)
#     print(space + bricks)
# appels = 5
# while appels > 0:
#     print("Я з'їв яблуко")
#     appels = appels - 1
#     print(f"Залишилось {appels}")
# print("Скінчилися яблука.... ")


# while True:
#     answer = input("Купи слона!")
#     if answer == "Так" or answer == "Ок":
#         print("Чудовий вибір!🐘")
#         break
#     else:
#         print(f"Усі кажуть {answer} , a купи слона")


# cart = ["", "", ""]
# while True:
#     item = input("Що купити?(stop):")
#     if item == "stop":
#         break
#     else:
#         cart.append(item)
# print(cart)
# print("Ваш чек:")
# for product in cart:
#     print(f"{product}")


# def calculate_total(price, quantity):
#     total = price * quantity
#     return total


# p = float(input("Введіть ціну яблук:"))
# q = input("Введіть кількість :")
# result = calculate_total(p, q)
# print(f"До сплати {result} гривень")


# import random


# print("Вітаємо у грі 'камінь,ножиці і  папір'!")
# print("Для виходу введи 'stop'")

# player_score = 0
# bot_score = 0

# options = ["камінь", "ножиці", "папір"]

# while True:
#     print("-" * 30)
#     print(f"РАХУНОК гравця {player_score}| Бот:{bot_score}")

#     user = input("\nТвій хід (камінь,ножиці,папір):")

#     if user == "stop":
#         print(f"Гра закінчена!Рахунок:{player_score}::{bot_score}")

#     if player_score > bot_score:
#         print("Ти переміг в матчі")
#     elif player_score < bot_score:
#         print("Бот виграв , ти лох...")
#     else:
#         print("Нічия")
#         break

#     if user not in options:
#         print("Ти дебіл!")
#         continue

#     computer = random.choice(options)
#     print(f"Комп'ютер обрав :{computer}")

#     if user == computer:
#         print("Нічия")
#     elif (
#         (user == "камінь" and computer == "ножиці")
#         or (user == "ножиці" and computer == "папір")
#         or (user == "папір" and computer == "камінь")
#     ):
#         print("Ти взяла цей раунд!")
#         player_score += 1
#     else:
#         print("Комп'ютер виграв...")
#         bot_score += 1


