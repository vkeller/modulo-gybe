from turtle import *
t = Turtle()

t.pencolor("blue")
t.pensize(4)
t.fillcolor('yellow') 
t.speed(0)

nbr = 12
pas = int(360/nbr)

for i in range(0,360,pas):
    t.begin_fill() 
    for _ in range(2):
        t.forward(100)
        t.left(30)
        t.forward(100)
        t.left(150)
    t.end_fill() 
    t.left(pas)