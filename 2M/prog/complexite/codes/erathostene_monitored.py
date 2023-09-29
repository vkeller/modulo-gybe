# Crible d'Eratosthène en Python monitoré
# Vincent Keller, 2023
import time

def erato(limite):
    # Intialisation du tableau
    tableau = []
    for i in range(limite):
        tableau.append(True)
    # Intialisation du tableau des entiers
    entiers = []
    tableau[0] = True
    tableau[1] = True
    # Crible en action
    for i in range(2,limite,1):
        if tableau[i] == True :
            for j in range(i*i,limite,i):
                tableau[j] = False
    # Création du tableau entiers en utilisant l'index du crible
    for i in range(limite):
        if tableau[i] == True:
            entiers.append(i)
    # Suppression des tableaux
    entiers.clear()
    tableau.clear()

limite = 10000000
for i in range(1000000,limite,50000):
    start = time.time()
    erato(i)
    end = time.time()
    print(i,"\t",(end-start))
