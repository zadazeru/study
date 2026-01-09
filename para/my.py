import random 
a = int(random.randint(6,24))
print(a)
n = a - 2
print('O' , end = '')
print('   ' * n, end = '')
print('O', end = '')
print('   ' * n, end = '')
print('O')
no = 0      
nx = n -1  
mx = 0      
mo = n - 1  
for i in range(n):
    print('O',end = '')
    for j in range(no):
        print('   ',end = '')
    print(' O ' , end='')
    for j in range(nx):
        print('   ', end='')
    print('O',end = '')
    for j in range(mo):
        print('   ',end = '')
    print(' O ' , end='')
    for j in range(mx):
        print('   ', end='')
    print('O',end = '')
    nx -= 1 
    no += 1  
    mo -= 1 
    mx += 1  
    print('')
print('O' , end = '')
print('   ' * n, end = '')
print('O', end = '')
print('   ' * n, end = '')
print('O')
    
    




