import random
borneInf = 0
borneSup = 100
atrouver = random.randint(borneInf,borneSup)
N = 0
nombre = 0
trouve = False
while (trouve!=True):
    if (nombre==atrouver):
        trouve=True
    nombre = nombre + 1
    N = N + 1
print("Nombre d'opérations pour trouver "+str(atrouver)+" : "+str(N))