
import sys
sys.stdout.reconfigure(encoding='utf-8')
from rich import print
from time import sleep

def type_line(text,char_delay):
    for char in text:
        print(f"[bold cyan] {char}[/bold cyan]", end="")
        sleep(char_delay)
    print()
    
def pritlyrics():
    lines = [
        ("Выходите, бесы💥,",0.05),
        ("мы станцуем jersey !",0.03),
        ("Отойди....",0.06),
        ("я войду....💯!",0.05),
        ("и она воскреснет вновь:D!",0.06),
        ("Пристегнись и смотри 👀, ",0.05),
        ("как тебе, Олеся🧕?",0.04),
        ("Жопа каждой из моих подруг в AMG обвесе!",0.05),
        ("Turn around 🧠, !",0.05),
        ("let me take my glock out!",0.05),
        ("Pop a round, let me see you drop down!",0.05)
    ]
        
    for line, char_delay in lines:
        type_line(line, char_delay)
        sleep(0.2)
pritlyrics()


        