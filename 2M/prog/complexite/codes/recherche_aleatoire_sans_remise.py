import random

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

borneInf = 0
borneSup = 100
atrouver = random.randint(borneInf,borneSup)
N = 0
trouve = False
deja_tire = []
while (trouve!=True):
    aleatoire = random_non_tire(deja_tire,borneInf,borneSup)
    if (aleatoire == atrouver) :
        trouve=True
    N = N + 1
    deja_tire.append(aleatoire)
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))
