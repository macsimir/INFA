from turtle import *
left(90)
pendown()
tracer(0)
k = 21

for i in range(13):
    forward(7*k)
    right(90)

penup()
for x in range(-10,10):
    for y in range(-10,10):
        setpos(x*k,y*k)
        dot(4)

done()
#49