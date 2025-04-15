from turtle import *

left(90)
pendown()
k = 60
tracer(0)
for i in range(130):
    forward(7*k)
    right(120)

penup()
for x in range(-10,10):
    for y in range(-10,10):
        setpos(x*k,y*k)
        dot(4)
update()
done()
