import math
from turtle import*
def heart_le(k):
    return 16*math.sin(k)**3

def heart_ri(k):
    return 15*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
    
speed(0)
bgcolor("black")
for i in range (8000):
    goto(heart_le(i)*20,heart_ri(i)*20)
    for j in range(4):
        color("red")
        goto(0,0)
done