N=15

for i in range(N):
    print(' x ', end='')  
print()
    
for i in range(N - 2):  
    print(' x', end='')    
    for i in range(N - 2):  
        print(' . ', end='')  
    print(' x ') 

for i in range(N):
    print(' x ', end='')
print()
