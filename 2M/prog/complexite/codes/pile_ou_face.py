import random
borneSup = 1000000
nbrPiles = 0
nbrFaces = 0
for i in range(borneSup):
    aleatoire = random.randint(0,1)
    if aleatoire == 1 :
        nbrPiles = nbrPiles + 1
    else:
        nbrFaces = nbrFaces + 1

print("Nombre de piles : ",nbrPiles)
print("Nombre de faces : ",nbrFaces)
