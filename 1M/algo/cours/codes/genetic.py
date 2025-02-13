# --------------------------------------------------
# Algorithme génétique : exemple
#
# Vincent Keller, Gymnase de Beaulieu, (c) 2025
# --------------------------------------------------
import random

# Fonction d'objectif
def fitness(individu):
    ret = 0
    for i in range(len(individu)):
        if individu[i] == 1:
            ret += 1
    return ret

taille = 100
longueur = 100
population = []
population_selected = []
pop_index = []

# paramètres de l'algorithme
taux_mutation = 0.05
taux_selection = 0.3
generations = 1000

# --------------------------------------------------
# Initialisation de la population
# --------------------------------------------------
for i in range(taille):
    individu = []
    for i in range(longueur):
        individu.append(random.randint(0,1))
    population.append(individu)

tmp = 0

for m in range(generations):
    fitness_global = 0
    pop_index.clear()
    
    # --------------------------------------------------
    # Evaluation
    # --------------------------------------------------
    for i in range(taille):
#        print("Individu",i,"fitness = ",fitness(population[i]))
        fitness_global += fitness(population[i])


    # --------------------------------------------------
    # Selection
    # --------------------------------------------------
    for i in range(taille):
        taux_s = random.random()
        if taux_s < taux_selection :
#            population_selected.append(population[i])
            pop_index.append(i)

#    if len(population_selected)%2 == 1:
    if len(pop_index)%2 == 1:
        index_plus = random.randint(0,len(population)-1)
#        population_selected.append(population[index_plus])
        pop_index.append(index_plus)

    # --------------------------------------------------
    # Crossover
    # --------------------------------------------------
#    for i in range(0,int(len(population_selected)),2):
    for i in range(0,int(len(pop_index)),2):
        point_of_crack = random.randint(0,longueur-1)
        for n in range(point_of_crack,longueur,1):
#            population_selected[i], population_selected[i+1] = population_selected[i+1], population_selected[i]
            population[pop_index[i]][n], population[pop_index[i+1]][n] = population[pop_index[i+1]][n], population[pop_index[i]][n]

    # --------------------------------------------------
    # Mutations
    # --------------------------------------------------
#    for i in range(0,int(len(population_selected)),2):
    for i in range(0,int(len(pop_index)),2):
        taux_s = random.random()
        if taux_s < taux_mutation :
            point_of_mutation = random.randint(0,longueur-1)
            if population[i][point_of_mutation] == 0:
                population[i][point_of_mutation] = 1
            else:
                population[i][point_of_mutation] = 0
#             if population_selected[i] == 0:
#                 population_selected[i] = 1
#             else:
#                 population_selected[i] = 0
    
    # Affichage fitness global
    print("Fitness global. Generation",m,":",fitness_global)