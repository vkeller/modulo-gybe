from turtle import *
t = Turtle()

t.pencolor("green")
t.pensize(2)
t.speed(0)

for i in range(500):
    t.forward(i)
    t.left(36)