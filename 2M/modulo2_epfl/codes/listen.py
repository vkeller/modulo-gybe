from turtle import *
from math import *
t = Turtle()

# Lambda calculus
def tracer(f, col='red'):
    color(col)
    for x in range(-300,300,10):
        goto(x,f(x))
        down()
    up()


def f():
    forward(20)

def haut():
    left(90)
    forward(10)
    right(90)
def bas():
    right(90)
    forward(10)
    left(90)
def gauche():
    left(180)
    forward(10)
    left(180)
def droite():
    forward(10)


s = getscreen()

# fonction souris
def f(x,y):
    up()
    goto(x,y)
    dot()
    write((x,y))
    down()


#Snake
#s.onkey(haut,'Up')
#s.onkey(bas,'Down')
#s.onkey(gauche,'Left')
#s.onkey(droite,'Right')
#s.listen()

# lambda
#tracer(sin,'red')

# Souris
s.onclick(f)
s.listen()
