from turtle import *

def triangle(cote,t) :
    i = 0
    while i < 3 :
        t.forward(cote)
        t.left(120)
        i += 1

tortue = Turtle()

couleur = "green"

if couleur != "red":
    print("Ce n'est pas la bonne coleur")
else:
    tortue.pencolor(couleur)

triangle(100, tortue)
