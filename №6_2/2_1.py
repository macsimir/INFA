from turtle import *

speed(0)
left(90)
pendown()
k = 1000

begin_fill()
for i in range(4):
    forward(111*k)
    right(120)
end_fill()


canvas = getcanvas()
cnt = 0

for x in range(-1000,1000):
    for y in range(-1000,1000):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
            cnt += 1 

print(cnt)
done()
