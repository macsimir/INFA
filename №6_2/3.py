from math import radians,tan

cnt = 0 
for x in range(-1000,1000):
    for y in range(-1000,1000):
        if x > 0 and y > tan(radians(30)) * x and y < tan(radians(150)) * x + 123:
            cnt += 1 

print(cnt)