from turtle import *

def branche(longueur, t):
    for i in range(5):
        t.forward(longueur)
        t.right(144)
        t.forward(longueur)
        t.left(72)

def etoile(nb_branches, longueur, t):
    angle = 360 / nb_branches
    for i in range(nb_branches):
        branche(longueur, t)
        t.right(angle)

tortue = Turtle()

couleur = "blue"

if couleur == "blue" or couleur == "red":
    tortue.pencolor(couleur)
else:
    print("Couleur non disponible, valeur par défaut : black")

etoile(5, 100, tortue)

done()
