import random
borneInf = 0
borneSup = 100
atrouver = random.randint(borneInf,borneSup)
N = 0
trouve = False
bmax = borneSup
bmin = borneInf
while (trouve!=True):
    moitie = int((bmax+bmin)/2)
    if (moitie == atrouver) :
        trouve=True
    elif (moitie > atrouver) :
        bmax = moitie
    elif (moitie < atrouver) :
        bmin = moitie
    N = N + 1
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))
