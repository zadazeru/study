import time
import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree():
    tree = [
        "        *        ",
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        " *************** ",
        "*****************",
        "       |||       ",
        "       |||       "
    ]

    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    end_color = '\033[0m'

    for line in tree:
        colored_line = ''.join(random.choice(colors) + ch + end_color if ch == '*' else ch for ch in line)
        print(colored_line)
        time.sleep(0.1)

def print_lyrics():
    lines = [
        ("Jingle Bells, Jingle Bells", 0.5),
        ("Jingle all the way", 0.5),
        ("Oh what fun it is to ride in a", 0.5),
        ("One horse open sleigh", 0.5),
        ("Jingle bells, Jingle Bells", 0.5),
        ("Jingle all the way", 0.5),
        ("Oh what fun it is to ride in a one", 0.5),
        ("Horse open sleigh!", 0.5),
    ]

    for line, delay in lines:
        print(line)
        time.sleep(delay)

if __name__ == "__main__":
    clear_console()
    print_tree()
    print()
    print_lyrics()
