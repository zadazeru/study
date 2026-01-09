a = [1, 1, 4, 3, 5, 6, 4, 3, 4, 7, 4, 2, 6, 8]
# Знаходимо мінімальний та максимальний елементи
min_e = min(a)
max_e = max(a)
# Обчислюємо абсолютне значення суми
as_N = abs(min_e + max_e)
# Створюємо список з as_N нулів
as_list = [0] * as_N
# Рахуємо скільки разів кожне число зустрічається
for i in range(len(a)):
    as_list[a[i]] += 1
    print(f"Індекс {i}: елемент = {a[i]}")
for i in range(len(as_list)):
    if as_list[i] > 0:
        print(f"Число {i}: {as_list[i]} разів")
