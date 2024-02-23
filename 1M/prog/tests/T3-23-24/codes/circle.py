from turtle import *

t = Turtle()

t.speed(1000)
def circle(r):
    t.penup()
    t.forward(r)
    t.left(90)
    t.pendown()
    for i in range(360):
        t.forward(r)
        t.left(1)
    t.penup()
    t.right(90)
    t.back(r) 
    t.pendown()

circle(1)
circle(2)