# В этой задаче мы делаем равно стороний треугольник
from math import *

cnt = 0 

for x in range(-1000,1000):
    for y in range(-1000,1000):
        # Условие для y , где 111 - это смещение 
        if x > 0 and y > tan(radians(30)) * x and y < tan(radians(150)) * x + 111:
            cnt += 1 

print(cnt)