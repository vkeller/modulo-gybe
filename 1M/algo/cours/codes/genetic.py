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


# paramètres de l'algorithme
taille = 100000
longueur = 8
population = []
population_selected = []
taux_mutation = 0.05
taux_crossover = 0.3
generations = 1000
type_select = 3 # 1 = roulette, 2 = tournoi, 3 = élitisme


# --------------------------------------------------
# Initialisation de la population
# --------------------------------------------------
for i in range(taille):
    individu = []
    for i in range(longueur):
        individu.append(random.randint(0,1))
    population.append(individu)

for m in range(generations):
    fitness_global = 0
    
    # --------------------------------------------------
    # Selection
    # --------------------------------------------------
    for i in range(0,taille,2):
        # 1. roulette
        if type_select == 1 :
            r = random.randint(0,1)
            if r == 1:
                population_selected.append(population[i])
                population_selected.append(population[i])
            else:
                population_selected.append(population[i+1])
                population_selected.append(population[i+1])            
        # 2. tournoi
#        elif type_select == 2 :


        # 3. élitisme
        elif type_select == 3 :
            if fitness(population[i]) >= fitness(population[i+1]) :
                population_selected.append(population[i])
                population_selected.append(population[i])
            else:
                population_selected.append(population[i+1])
                population_selected.append(population[i+1])
        
        else:
            print("Choisissez un type de sélection de population (1,2, ou 3 voir doc)")
            break

    # --------------------------------------------------
    # Crossover
    # --------------------------------------------------
    for i in range(0,int(len(population_selected)),2):
        prob = random.random()
        if prob < taux_crossover :
            point_of_crack = random.randint(0,longueur-1)
            for n in range(point_of_crack,longueur,1):
                population_selected[i], population_selected[i+1] = population_selected[i+1], population_selected[i]

    # --------------------------------------------------
    # Mutations
    # --------------------------------------------------
    for i in range(0,int(len(population_selected)),2):
        taux_s = random.random()
        if taux_s < taux_mutation :
            point_of_mutation = random.randint(0,longueur-1)
            if population_selected[i][point_of_mutation] == 0:
                population_selected[i][point_of_mutation] = 1
            else:
                population_selected[i][point_of_mutation] = 0

    # --------------------------------------------------
    # Evaluation globale
    # --------------------------------------------------
    for i in range(taille):
        fitness_global += fitness(population_selected[i])
    print("Fitness global. Generation",m,":",fitness_global)



    population.clear()
    for i in range(taille):
        population.append(population_selected[i])
    population_selected.clear()