from turtle import *

t = Turtle()

t.shape('turtle')
t.pensize(3)
t.speed(1)

def triangle(taille, couleur):
    t.pencolor(couleur)
    t.fillcolor(couleur)
    t.begin_fill()
    for i in range(3):
        t.forward(taille)
        t.left(120)
    t.end_fill()
        
def carre(taille, couleur):
    t.pencolor(couleur)
    t.fillcolor(couleur)
    t.begin_fill()
    for i in range(4):
        t.forward(taille)
        t.left(90)
    t.end_fill()

def maison(taille, couleur_bloc, couleur_toit):
    carre(taille, couleur_bloc)
    t.penup()
    t.left(90)
    t.forward(taille)
    t.right(90)
    t.pendown()
    triangle(taille, couleur_toit)
    t.penup()
    t.right(90)
    t.forward(taille)
    t.left(90)
    t.pendown()
    
maison(50,'red', 'red')

t.penup()
t.forward(80)
t.pendown()

maison(100,'cyan', 'blue')

t.penup()
t.back(200)
t.pendown()

t.pensize(5)
t.pencolor('green')
t.forward(400)
t.penup()
t.back(350)
t.pendown()

t.pensize(7)
t.fillcolor("brown")
t.begin_fill()
for i in range(2):
    t.pencolor("brown")
    t.forward(10)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

t.pensize(15)
t.fillcolor("green")
t.pencolor('green')
t.begin_fill()
t.circle(80)
t.end_fill()

