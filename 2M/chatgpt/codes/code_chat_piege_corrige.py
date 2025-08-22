from turtle import *

def branche(longueur, t):
    """Dessine une seule branche d'étoile."""
    t.forward(longueur)
    t.right(144)

def etoile(nb_branches, longueur, t):
    """Dessine une étoile complète en répétant les branches."""
    for i in range(nb_branches):
        branche(longueur, t)

# Création de la tortue
tortue = Turtle()
tortue.speed(0)

couleur = "blue"

# Choix de la couleur
if couleur == "blue" or couleur == "red":
    tortue.pencolor(couleur)
else:
    print("Couleur non disponible, valeur par défaut : black")
    tortue.pencolor("black")

# Dessin
etoile(5, 200, tortue)

done()
