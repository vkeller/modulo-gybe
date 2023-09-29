import random
borneInf = 0
borneSup = 10
# Création d'une liste vide
maListe = []
# Création d'une liste de nombre aléatoires
for i in range(borneSup):
    aleatoire = random.randint(borneInf,borneSup)
    maListe.append(aleatoire)
# Calcul de la somme de tous les nombres de la liste
somme = 0
i = 0
while i < len(maListe):
    somme = somme + maListe[i]
    i = i + 1
print("Somme   ",somme)
print("Moyenne ",(somme/borneSup))