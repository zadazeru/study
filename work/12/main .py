# # def generate_full_name(firsdnname,lastname):
# #     space = ''
# #     fullname = firsdnname+lastname
# #     return fullname  import mymodule
# # print(mymodule.generate_full_name('Asabeneh', ' Yetayeh'))

# # main.py file
# from mymodule import generate_full_name, sum_two_nums, person, gravity
# print(generate_full_name('Asabneh','Yetay'))
# print(sum_two_nums(1,9))
# mass = 100
# weight = mass * gravity
# print(weight)
# print(person['firstname'])

import pygame
import random
import sys

# --- НАЛАШТУВАННЯ ---
WIDTH = 800  # ширина вікна
HEIGHT = 600  # висота вікна
NUM_DROPS = 150  # кількість крапель
DX = 10  # зсув по X (вправо)
DY = 8  # зсув по Y (вниз)
BG_COLOR = (0, 0, 0)  # чорний фон
DROP_COLOR = (0, 255, 0)  # зелений "кібердощ" :)
DROP_LENGTH = 15  # довжина однієї краплі у пікселях
FPS = 60  # кадрів за секунду


def create_drops():
    """
    Створює список крапель.
    Кожна крапля - це [x, y].
    x: від 0 до WIDTH
    y: від -HEIGHT до 0, щоб частина крапель з'являлась "зверху"
    """
    return [
        [random.randint(0, WIDTH), random.randint(-HEIGHT, 0)] for _ in range(NUM_DROPS)
    ]


def move_drops(drops):
    """
    Рухаєм кожну краплю: вниз і трохи вправо.
    Якщо крапля виходить за низ екрану — повертаємо її наверх.
    """
    for drop in drops:
        drop[0] += DX
        drop[1] += DY

        # Якщо крапля вилетіла за нижній край або далеко вправо —
        # перенесемо її наверх у випадкове місце
        if drop[1] > HEIGHT or drop[0] > WIDTH + 50:
            drop[0] = random.randint(0, WIDTH)
            drop[1] = random.randint(-HEIGHT, 0)


def draw_drops(screen, drops):
    """
    Малюємо всі краплі як маленькі вертикальні лінії.
    """
    for x, y in drops:
        start_pos = (x, y)
        end_pos = (x, y + DROP_LENGTH)
        pygame.draw.line(screen, DROP_COLOR, start_pos, end_pos, 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rain animation")
    clock = pygame.time.Clock()

    # початковий список крапель
    drops = create_drops()

    running = True
    while running:
        # --- ОБРОБКА ПОДІЙ ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- ЛОГІКА ---
        move_drops(drops)

        # --- МАЛЮВАННЯ ---
        screen.fill(BG_COLOR)  # очистка екрана
        draw_drops(screen, drops)  # малюємо всі краплі

        pygame.display.flip()  # показати кадр

        clock.tick(FPS)  # обмежуємо FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
