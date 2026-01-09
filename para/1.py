
N = 15

for i in range(N):
    print(' @ ', end='')
print()

for i in range(N - 2):
    print(' @ ', end='')
    for i in range(N - 2):
        print(' . ', end='')
    print(' @ ')

for i in range(N):
    print(' @ ', end='')
print()