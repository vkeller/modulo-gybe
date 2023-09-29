# Crible d'Eratosthène en Python
# Vincent Keller, 2023
limite = 100
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
print(entiers)