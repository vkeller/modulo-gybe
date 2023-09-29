# Bubble sort example monitoré
# Vincent Keller, 2023 
import random
import time
def bubble(longueur):
    nombres = []
    ## Remplissage de la liste
    for i in range(longueur):
        aleat = random.randint(0,longueur)
        nombres.append(aleat)
    ## Bubble sort itself
    for i in range(longueur,0,-1):
        for j in range(0,i-1,1):
            if nombres[j+1] < nombres[j]:
                tmp = nombres[j+1]
                nombres[j+1] = nombres[j]
                nombres[j] = tmp
    # Destruction des tableaux
    nombres.clear()

limite = 10000
for i in range(1000,limite,200):
    start = time.time()
    bubble(i)
    end = time.time()
    print(i,"\t",(end-start))