from turtle import *

def petale(longueur, angle, t):
    for i in range(2):
        t.forward(longueur)
        t.left(angle)
        t.forward(longueur)
        t.right(2 * angle)

def fleur(nombre_petales, longeur, t):
    compteur = 0
    while compteur < nombre_petales:
        petal(longeur, 60, t)
        t.right(360 / nombre_petales)

tortue = turtle()

couleur = "yellw"

if couleur ==! "yellow":
    tortue.Pencolor(couleur)
else:
    print("Couleur non reconnue")

fleur(6, 100, tortue)

done()
