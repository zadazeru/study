# from os import name
# import select
# from socket import herror
# from unittest import mock

from pyclbr import Class
from re import A
import time
import random


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
        self.max_health = health

    def get_health(self):
        return self.__health

    def is_alive(self):
        return self.__health > 0

    def take_damage(self, damage):
        self.__health -= damage  # Мінус дорівнює! Не просто дорівнює.
        if self.__health < 0:
            self.__health = 0
        print(
            f"{self.name} отримав {damage} HP. (Залишилося: {self.__health}/{self.max_health})"
        )

    def attack(self, enemy):
        print(f"{self.name} намагається атакувати")


class Mage(Hero):
    def attack(self, enemy):
        damage = random.randint(10, 25)
        print(f"{self.name} кастує вогняну кулю в {enemy.name}")
        enemy.take_damage(damage)


class Warrior(Hero):
    def attack(self, enemy):
        damage = random.randint(10, 25)
        print(f"{self.name} рубає сокирою {enemy.name}!")
        enemy.take_damage(damage)


class Archer(Hero):
    def attack(self, enemy):
        damage = random.randint(5, 15)
        print(f"{self.name} стріляє стрілою в {enemy.name}")
        enemy.take_damage(damage)


mage = Mage("Сіріус", 100)
acher = Archer("Літініус", 80)
warrior = Warrior("Вітінг", 80)
print(f"Починається дуель ..{mage.name} проти {warrior.name}! ")
print(f"Починається дуель між {mage.name}  проти {acher.name}")
print("-" * 40)
time.sleep(1)

round_1 = 1

while mage.is_alive() and warrior.is_alive():
    print(f"\n Раунд {round_1}")

    mage.attack(warrior)
    if not warrior.is_alive():
        print(f"{warrior.name}  впав!! {mage.name} переміг ")
        break
    time.sleep(1)

    warrior.attack(mage)
    if not mage.is_alive():
        print(f"{mage.name} переміг {warrior.name}... поразка")
        break
    time.sleep(1)
    round_1 += 1
print("-" * 40)
print("Бій завершений")


# class Student:
#     def __init__(self, name, age, course):
#         self.age = age
#         self.name = name
#         self.course = course

#     def say_hello(self):
#         print(f"Привіт .Мене звати {self.name} ,мені {self.age}   ")

#     def study(self):
#         print(f"На даний момент я навчаюся {self.course} курсі")


# Student1 = Student("Дарина", 18, 2)
# Student2 = Student("Роман", 20, 3)
# Student1.say_hello()
# Student2.say_hello()
# Student1.study()
# Student2.study()


# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.__health = health

#     def show_stats(self):
#         print(f"Здоров'я {self.name}: {self.__health}")

#     def move(self):
#         print(f"{self.name} біжить...")

#     def damage_a(self, damage):
#         self.__health -= damage
#         print(f"{self.name} отрмав {damage} урону! Залишилося{self.__health}")

#     def get_health(self):
#         return self.__health


# hero = Hero("Arats", 100)
# print(f"Перевірка через метод: {hero.get_health()}")
# hero.damage_a(20)


# class Mage(Hero):
#     def cast_spell(self):
#         print(f"{self.name} кидай сокиру")

#     def attack(self):
#         print(f"{self.name} атакує магією")


# class Warrior(Hero):
#     def attack(self):
#         print(f"Тут {self.name} б'є мечем")
#         print(f"{self.name} атакує сокирою")


# team = [Mage("Merlin", 50), Warrior("Arthur", 100)]
# print("--- БІЙ ПОЧИНАЄТЬСЯ ---")
# for hero in team:
#     hero.attack()
#     hero.move()
#     print("-" * 20)


# print("Окремі герої")
# player1 = Mage("Gendaf", 80)
# player1.move()
# player1.cast_spell()

# woin = Warrior("Conan", 150)
# woin.attack()

# print(woin.get_health())
# def show_hero(self):
#     print(f"Герой на ім'я {self.name} має {self.health} здоров'я")

# def heal(self, amount):
#     self.health += amount
#     print(f"Герой підклікувався на {amount}.Тепер його здоров'я {self.health}")


# hero1 = Hero("Arats", 100)
# hero1.show_hero()
# hero1.heal(50)
# hero1.show_hero
