# Calcul de la table de la multiplication des entiers
# Vincent Keller, 2023

taille = 10

# Nombre d'opérations ou d'instructions
N = 0

for t in range(100,5000,100):
    N = 0
    taille = t
    for i in range(taille):
        for j in range(taille):
            multiplication = i * j
            N = N + 1
    print(taille, "\t",N)



