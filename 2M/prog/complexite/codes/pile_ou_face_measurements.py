import random
import time
start = time.time()
for i in range(100):
    borneSup = 10000
    nbrPiles = 0
    nbrFaces = 0
    for i in range(i*borneSup):
        aleatoire = random.randint(0,1)
        if aleatoire == 1 :
            nbrPiles = nbrPiles + 1
        else:
            nbrFaces = nbrFaces + 1
    end = time.time()
    print(nbrPiles, nbrFaces, i*borneSup, (end-start))
print("Nombre de piles : ",nbrPiles)
print("Nombre de faces : ",nbrFaces)
print("Nombre de tirs  : ",borneSup)
print("Time            : ",(end-start))
