## Bubble sort example
import random
nombres = []
longueur = 10
## Remplissage de la liste
for i in range(longueur):
    aleat = random.randint(0,longueur)
    nombres.append(aleat)
print(nombres)
## Bubble sort itself
for i in range(longueur,0,-1):
    for j in range(0,i-1,1):
        if nombres[j+1] < nombres[j]:
            tmp = nombres[j+1]
            nombres[j+1] = nombres[j]
            nombres[j] = tmp
print(nombres)