from turtle import *
t = Turtle()

t.pencolor("black")
t.pensize(2)
t.speed(0)

taille = 100

t.fillcolor('blue') 
t.begin_fill()
i = 0
while i < 4:
    t.forward(taille)
    t.left(90)
    i = i + 1
t.end_fill() 
t.fillcolor('red')
t.penup()
t.left(90)
t.forward(taille)
t.right(90)
t.pendown()
t.begin_fill() 
i = 0
while i < 3 :
    t.forward(taille)
    t.left(120)
    i = i + 1
t.end_fill() 
t.penup()
t.right(90)
t.forward(taille)
t.left(90)
t.pendown()