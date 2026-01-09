# Writing RegEx Patterns
import re

regex_pattern = r"apple"
txt = "Apple and banana are fruits.An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
match = re.findall(regex_pattern, txt)
print(match)
match = re.findall(regex_pattern, txt, re.I)
print(match)

regex_pattern = r"[Aa]pple"
matches = re.findall(regex_pattern, txt)
print(matches)


regex_pattern = r"[Aa]pple|[Bb]anana"
txt = "Apple and Banana are fruits.An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"\d"
txt = "This regular expression example was made on December ^, 2019 and revised on July 8, 2021"
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"\d+"
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"[a].*"
txt = """Apple and banana are fruits"""
match = re.findall(regex_pattern, txt)
print(match)

txt = """I am not sure if there is a converntion how to write the word e-mail.Some people write it as email other may write as Email or E-mail"""
regex_pattern = r"[Ee]-?mail"
match = re.findall(regex_pattern, txt)
print(match)
