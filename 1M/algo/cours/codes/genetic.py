import random

# Fonction d'objectif
def fitness(individu):
    ret = 0
    for i in range(len(individu)):
        if individu[i] == 1:
            ret += 1
    return ret

taille = 10
longueur = 8
population = []

# paramètres de l'algorithme
taux_mutation = 0.02
taux_combinaison = 0.5

for i in range(taille):
    individu = []
    for i in range(longueur):
        individu.append(random.randint(0,1))
    population.append(individu)

for i in range(taille):
    print("Individu",i,"fitness = ",fitness(population[i]))
