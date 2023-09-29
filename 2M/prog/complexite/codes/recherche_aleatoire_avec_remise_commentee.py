# Recherche aléatoire avec remise dans une liste triée commentée 
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
# Boucle "tant que la variable trouve n'est pas égale à True)
while (trouve!=True):
    # On tire un nombre que l'on assigne à la variable aleatoire
    aleatoire = random.randint(borneInf,borneSup)
    # Si le nombre à trouver est égal au nombre aléatoire tiré, alors on sort de la boucle
    if (aleatoire == atrouver) :
        trouve=True
    # On incrémente le nombre de comparaisons
    N = N + 1
# Output : affichage du nombre à trouver et du nombre de comparaisons
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))


