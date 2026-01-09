import re
from unittest import result
from collections import Counter

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

# Список слів для пошуку
words_to_find = [
    "love",
    "you",
    "can",
    "what",
    "teaching",
    "not",
    "else",
    "do",
    "I",
    "which",
    "to",
    "the",
    "something",
    "if",
    "give",
    "develop",
    "capabilities",
    "application",
    "an",
    "all",
    "Python",
    "If",
]

# Підраховуємо частоту кожного слова
results = []
for word in words_to_find:
    # Пошук без урахування регістру
    matches = re.findall(r"\b" + word + r"\b", paragraph, re.IGNORECASE)
    count = len(matches)
    results.append((count, word))

# Сортуємо за кількістю (спадаючий порядок)
results.sort(reverse=True)
# # Виводимо результати
# print("Частота слів:")
# for count, word in results:
#     print(f"  ({count}, '{word}')")

# Найчастіше слово
most_common = results[0]
print(f"\nНайчастіше слово: '{most_common[1]}' - {most_common[0]} разів")

litle_common = results[-1]
print(f"Найменш частіше слово:'{litle_common[1]}' - {litle_common[0]} разів")
