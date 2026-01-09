import random 

a = int(random.randint(6,24))
print(a)

n = a - 2
no = n - 1
nx = 0
mx = n - 1
mo = 0

print('O' , end = '')
print(' - ' * n, end = '')
print('O', end = '')
print(' - ' * n, end = '')
print('O')
for i in range(n):
    print('O',end = '')
    for j in range(no):
        print(' - ',end = '')
    print(' O ' , end='')
    for j in range(nx):
        print(' - ', end='')
    