import re

text = "Сьогодні новий рік - 2026. Перший місяць і другий день зими"
num = re.findall(r"\d+", text)
print(num)


email_fin = "Щоб створити свій обліковий запис нам потрібно ввести вигадану  електронну пошту - darinazigula#gmail.com та придумати свій пароль"
email = re.findall(r"[\w\.]+@\w+\.\w+", email_fin)
print(email)


data_anal = "Замовлення №4591 від клієнта (097) 123-45-67. Сума: 1200 грн. Інше замовлення №9910, телефон +380509999999. Сума 500$."
data_fin_number = re.findall(r"№\d+", data_anal)
print(f"Замовлення {data_fin_number}:")

data_money = re.findall(r"\d+\s?(?:грн|\$)", data_anal)
print(f"Сума {data_money}")

phones = re.findall(r"[\d|+\-\(\)\s]{10,}", data_anal)
print(phones)


txt = "I can coding in Python"
match = re.match("I can coding ", txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)
substring = txt[start:end]
print(substring)


txt_two = txt = (
    " i like learning Python but i dont have enought time to coding my practice question"
)
match = re.search("enought time", txt_two, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt_two[start:end]
print(substring)


txt_three = "I Wanna be your girl  GIRL Girl,i wanna kiss your lipss . I dont wanna be afraid when you dreaming me."
match = re.findall("wanna", txt_three, re.I)
match_two = re.findall("girl|GIRL|Girl", txt_three)
print(match, match_two)

txt_four = "Python is the most beautiful language that a human being has ever created. I reccomend python for a first language for beginner person who want "
match_four = re.sub("Python|python", "JavaScript", txt_four, re.I)
print(match_four)


txt = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

matches = re.sub("%", "", txt)
print(matches)

txt = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""
print(re.split("\n", txt))  # splitting using \n - end of line symbol
