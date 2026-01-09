N=6

for i in range(N+1): #перша лінія
    print(' x ', end='')  
print()
    
for i in range(N - 3):  #бокові лінії -
    print('x', end='') # пробіл у боковій лінії = рух вправо     
    for i in range(N+3):  
        print('  ', end='')  #пробіл x
    print(' x ') 

for i in range(N+1):
    print(' x ', end='')
print()