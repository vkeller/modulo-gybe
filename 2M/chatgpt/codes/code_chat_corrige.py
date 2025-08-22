from turtle import *

def petale(longueur, angle, t):
    for i in range(2):
        t.forward(longueur)
        t.left(angle)
        t.forward(longueur)
        t.right(2 * angle)

def fleur(nombre_petales, longueur, t):
    compteur = 0
    while compteur < nombre_petales:
        # appel de fonction incorrect
        petale(longueur, 60, t)
        t.right(360 / nombre_petales)
        # Boucle infinie
        compteur += 1

# Nom de la classe avec majuscule
tortue = Turtle()

# Nom de couleur incorrect
couleur = "yellow"

# Opérateur de comparaison incorrect
if couleur != "yellow":
    # méthode Pencolor() incorrect
    tortue.pencolor(couleur)
else:
    print("Couleur non reconnue")

fleur(6, 100, tortue)

done()

