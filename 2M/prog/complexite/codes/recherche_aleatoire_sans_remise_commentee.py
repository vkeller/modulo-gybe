# Recherche aléatoire sans remise commentée
# On ne tire jamais le même nombre aléatoire à chaque itération
# Vincent Keller, 2023

# Importation de la bibliothèque random (nombres aléatoires)
import random

# Définition d'une fonction qui retourne un nombre aléatoire qui n'a jamais été tiré
# Argument 1 : already : liste qui contient tous les nombres aléatoires déjà tirés
# Argument 2 : bmin : borne inférieure pour la fonction randint
# Argument 3 : bmax : borne supérieure pour la fonction randint
# Return     : un nombre aléatoire jamais tiré auparavant
# ATTENTION : CETTE FONCTION EST PARTICULIEREMENT COMPLEXE, VOUS N'AVEZ PAS BESOIN D'EN COMPRENDRE
# TOUTES LES SUBTILITES
def random_non_tire(already,bmin,bmax):
    ret = 0
    nontire = False
    while nontire != True :
        aleat = random.randint(bmin,bmax)
        tire = False
        for i in range(len(already)):
            if already[i] == aleat :
                tire = True
        if tire == False:
            nontire = True
    return aleat


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
# deja_tire est une liste qui contient tous les nombres aléatoires déjà tirés
# Initialisation à une liste vide
deja_tire = []
# Boucle "tant que la variable trouve n'est pas égale à True)
while (trouve!=True):    
    # On tire un nombre jamais tiré que l'on assigne à la variable aleatoire
    aleatoire = random_non_tire(deja_tire,borneInf,borneSup)
    # Si le nombre à trouver est égal au nombre aléatoire tiré, alors on sort de la boucle
    if (aleatoire == atrouver) :
        trouve=True
    # On incrémente le nombre de comparaisons
    N = N + 1
    # on ajoute le nombre à la liste des aléatoires déjà tirés
    deja_tire.append(aleatoire)
# Output : affichage du nombre à trouver et du nombre de comparaisons
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))

