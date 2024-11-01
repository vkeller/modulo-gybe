from turtle import *
t = Turtle()
t.pencolor('green')
t.pensize(3)
t.speed(40)
nbr = 30
for i in range(nbr):
    t.forward(100)
    t.left(30)
    t.forward(100)
    t.left(150)
    t.forward(100)
    t.left(30)
    t.forward(100)
    t.left(150)
    t.right(360/nbr)
