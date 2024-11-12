from turtle import *
t = Turtle()

t.pencolor("black")
t.pensize(2)
t.speed(0)

t.penup()
t.back(200)
t.pendown()

taille = 60
nbrMaisons = 6

for _ in range(1):
    for i in range(nbrMaisons):
        t.fillcolor('blue') 
        t.begin_fill() 
        for i in range(4):
            t.forward(taille)
            t.left(90)
        t.end_fill() 
        t.fillcolor('red')
        t.penup()
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.pendown()
        t.begin_fill() 
        for i in range(3):
            t.forward(taille)
            t.left(120)
        t.end_fill() 
        t.penup()
        t.right(90)
        t.forward(taille)
        t.left(90)
        t.forward(taille + 20)
        t.pendown()

    t.penup()
    t.back((taille+20)*nbrMaisons)
    t.right(90)
    t.forward(taille*3)
    t.left(90)
    t.pendown()
