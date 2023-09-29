## Insertion sort example
import random
nombres = []
longueur = 10
## Remplissage de la liste
for i in range(longueur):
    aleat = random.randint(0,longueur)
    nombres.append(aleat)
print(nombres)
## Insertion sort itself
j = 1
while j <= longueur-1:
    i = j - 1
    k = nombres[j]
    while i >= 0 and nombres[i] > k:
        nombres[i+1] = nombres[i]
        i = i - 1
    nombres[i+1] = k
    j = j + 1
print(nombres)