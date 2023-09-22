import random
borneInf = 0
borneSup = 100
atrouver = random.randint(borneInf,borneSup)
N = 0
trouve = False
while (trouve!=True):
    aleatoire = random.randint(borneInf,borneSup)
    if (aleatoire == atrouver) :
        trouve=True
    N = N + 1
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))

