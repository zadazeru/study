n = 5  # высота пирамиды

for i in range(1, n + 1):
    stars = 2 * i - 1
    spaces = n - i
    print(" " * spaces + "x" * stars)
    