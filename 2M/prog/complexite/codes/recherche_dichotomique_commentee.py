# Recherche dichotomique commentée
# Vincent Keller, 2023

# Importation de la bibliothèque random (nombres aléatoires)
import random
# Input borneInf
borneInf = 0
# Input borneSup
borneSup = 100
# variable atrouver : nombre aléatoire de type entier compris entre borneInf et borneSup (compris)
atrouver = random.randint(borneInf,borneSup)
# N est la variable qui contiendra le nombre de comparaisons
N = 0
# trouve est une variable de type booléen.
trouve = False
# déclaration de la variable bmax qui contient la borne supérieure temporaire après division par 2
# A l'initialisation, elle contient la borne supérieure globale borneSup
bmax = borneSup
# déclaration de la variable bmin qui contient la borne inférieure temporaire après division par 2
# A l'initialisation, elle contient la borne inférieure globale borneInf
bmin = borneInf
# Boucle "tant que la variable trouve n'est pas égale à True)
while (trouve!=True):
    # on calcule l'élément à la moitié des deux bornes temporaires
    moitie = int((bmax+bmin)/2)
    # si moitie est égal au nombre à trouver, on sort de la boucle
    if (moitie == atrouver) :
        trouve=True
    # sinon, si le nombre à trouver est situé avant de la moitié, alors la borne supérieure
    # temporaire devient moitie
    elif (moitie > atrouver) :
        bmax = moitie
    # sinon, si le nombre à trouver est situé au-delà de la moitié, alors la borne inférieure
    # temporaire devient moitie
    elif (moitie < atrouver) :
        bmin = moitie
    # On incrémente le nombre de comparaisons
    N = N + 1
# Output : affichage du nombre à trouver et du nombre de comparaisons
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))

