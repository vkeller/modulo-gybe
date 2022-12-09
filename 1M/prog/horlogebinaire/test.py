from turtle import *
from math import *
t = Turtle()

colormode(255)
couleur = (41,41,253)
t.pencolor(couleur)
t.speed(100)

taille = 30
espace = 10

def bit_heure():
    deplace_demi()
    t.circle(taille/2)

def bit_minute():
    t.left(45)
    t.forward(sqrt(taille*taille*2))
    t.penup()
    t.left(135)
    t.forward(taille)
    t.left(135)
    t.pendown()
    t.forward(sqrt(taille*taille*2))
    t.penup()
    t.right(135)
    t.forward(taille)
    t.left(180)
    t.pendown()

def bit_second():
    for i in range(4):
        t.forward(taille)
        t.left(90)

def deplace():
    t.penup()
    t.forward(taille+espace)
    t.pendown()

def deplace_demi():
    t.penup()
    t.forward(taille/2)
    t.pendown()

bit_minute()
deplace()
bit_minute()
deplace()
bit_second()
deplace()
bit_heure()




#t.begin_fill()
#for i in range(n):
#    t.forward(100)
#    t.left(360/n)
#t.forward(300)
#t.right(90)
#t.forward(100)
#t.end_fill()