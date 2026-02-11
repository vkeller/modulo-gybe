# -------------------------------------------------------------
# Générateur de mots aléatoires de 7 lettres
# Vincent Keller (c) 2026
# -------------------------------------------------------------
import random

def init_individu():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    j = 0
    mot = ""
    while j < 7:
        pos = random.randint(1,26)
        mot = mot + alphabet[pos-1]
        j = j + 1
    return mot

def fitness(individu,cible):
    i = 0
    fit = 0
    while i < len(individu):
        if individu[i] == cible[i]:
            fir = fit + 1
        i = i + 1
    return fit

def selection(pop,cible):
    i = 0
    fit_pop = []
    while i < len(pop):
       fit_pop.append(fitness(pop[i],cible))
    i = i + 1
    
population = []
i = 0
while i < 2:
    population.append(init_individu())
    i = i + 1
print(population)

secret = input("Quel mot à rechercher : ")

generations = 10

g = 0
while g < generations:
    selection(population)
