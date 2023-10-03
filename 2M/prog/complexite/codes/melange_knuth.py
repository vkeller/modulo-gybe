# Algorithme de mélange de Knuth
# Permet de mélanger une liste par permutation aléatoire
# Vincent Keller, 2023
import random

borneSup = 10

liste = []

for i in range(borneSup):
    liste.append(i)

print(liste)

for i in range(borneSup-1,1,-1):
    j = random.randint(0,i)
    tmp = liste[i]
    liste[i] = liste[j]
    liste[j] = tmp

print(liste)
