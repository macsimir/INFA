from turtle import *

k = 20
left(90)
tracer(0)
pendown()

right(45)
forward(5*k)
for i in range(7):
    right(45)
    forward(16*k)
    right(135)
    forward(8*k)
penup()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k, y*k)
        dot(3)
done()

# Считаем кол -во точек и получаем 90 