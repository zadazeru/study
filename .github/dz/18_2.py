import re
from collections import Counter
# import sys

# sys.stdout.reconfigure(encoding="utf-8")
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."


# def top_10_words(text):
#     pattern = r"[a-z]+"
#     words = re.findall(pattern, text.lower())
#     count = Counter(words)
#     return count.most_common(10)


# try:
#     top_10 = top_10_words(paragraph)
#     print("Топ 10 слів у тексті :")
#     for word, frequency in top_10:
#         print(f"Слово '{word}' зустрічається {frequency} разів")

# except Exception as e:
#     print(f"Сталася помилка")

words = re.findall(r"\w+", paragraph.lower())
count = Counter(words)
top_counter = count.most_common(1)
most_f = top_counter[0][0]
freq = top_counter[0][1]
print(f"НАйчастіше слова {most_f}")
print(f"Воно зустрічається {freq} разів")


points = ["-12", "-4", "-3", "-1", "0", "4", "8"]
num_poison = [int(i) for i in points]
num_poison.sort()
print(f"Відсортовані списки:{num_poison}")
smalles = num_poison[0]
larges = num_poison[-1]
distance = larges - smalles
print(f"Відстань між точками :{distance}")


def is_valid_variable(name):
    patter = r"^[a-zA-Z_]\w*$"
    if re.search(patter, name):
        return True
    else:
        return False


print(is_valid_variable("firstname"))  # True
print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # True
print(is_valid_variable("firstname"))  # True

# Сміття
sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
match = re.sub(r"[%$@#&]", "", sentence)
print(match)
