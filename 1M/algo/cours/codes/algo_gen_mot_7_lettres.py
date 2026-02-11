# -------------------------------------------------------------
# Générateur de mots aléatoires de X lettres (x est la longueur)
# Vincent Keller, Gymnase de Beaulieu, (c) 2026
# -------------------------------------------------------------
import random

longueur = 7
taille_population = 4000 # Doit être pair !
generations = 30
taux_mutation = 1 # Compris entre 1 et 6 (dé à jouer)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def init_individu():
    j = 0
    mot = ""
    while j < longueur:
        pos = random.randint(1,26)
        mot = mot + alphabet[pos-1]
        j = j + 1
    return mot

def fitness(individu,cible):
    i = 0
    fit = 0
    while i < len(individu):
        if individu[i] == cible[i]:
            fit = fit + 1
        i = i + 1
    return fit

def selection(pop,cible):
    i = 0
    fit_pop = []
    sel_pop = []
    while i < len(pop):
        ind = [pop[i],fitness(pop[i],cible)]
        fit_pop.append(ind)
        i = i + 1
    i = 0
    # Tri de la liste en fonction des fitness
    fit_pop = sorted(fit_pop,key=lambda x: x[1])
    i = taille_population - 1
    while i >= 0:
        sel_pop.append(fit_pop[i][0])
        i = i - 1
    # Renvoi d'une liste de taille taille_population (les taille_population plus forts)
    return sel_pop

def crossover(ind1,ind2):
    new_ind1 = ""
    new_ind2 = ""
    i = 0
    # Point de mutation (pour le jeu, 1 à 6 fonctionne)
    point = random.randint(1,longueur)
    while i < len(ind1):
        if i < point:
            new_ind1 = new_ind1 + ind1[i]
            new_ind2 = new_ind2 + ind2[i]
        else:
            new_ind1 = new_ind1 + ind2[i]
            new_ind2 = new_ind2 + ind1[i]
        i = i + 1
    return new_ind1, new_ind2

def mutation(ind):
    point = random.randint(1,longueur)
    new_ind = ""
    i = 0
    while i < longueur:
        if i == point:
            pos = random.randint(1,26)
            new_ind = new_ind + alphabet[pos-1]
        else:
            new_ind = new_ind + ind[i]
        i = i + 1
    return new_ind

## INITIALISATION
population = []
i = 0
while i < taille_population:
    population.append(init_individu())
    i = i + 1

secret = input("Quel mot à rechercher : ")
secret = secret.upper()

## GENERATIONS
g = 0
while g < generations:
    ## SELECTION
    sel = selection(population, secret)
    fit_max = 0

    ## CROSSOVER
    i = 0
    while i < taille_population:
        ind1, ind2 = crossover(sel[i], sel[i+1])
        sel[i] = ind1
        sel[i + 1] = ind2
        i = i + 2
        
    ## MUTATION
    i = 0
    while i < taille_population:
        mut = random.randint(1,6)
        if mut < taux_mutation :
            sel[i] = mutation(sel[i])
        i = i + 1
    # A-T-ON TROUVE LE SECRET ?
    i = 0
    while i < taille_population:
        fit = fitness(sel[i], secret)
#        print(sel[i],fit)
        if fit == longueur:
            print("Mot secret trouvé : ",sel[i],"à la génération",g)
            # permet de sortir de la boucle
            g = generations + 1
        i = i + 1
    ## RECOPIE DE LA POP SEL VERS LA POPULATION
    population.clear()
    population = sel.copy()
    sel.clear()
    g = g + 1
