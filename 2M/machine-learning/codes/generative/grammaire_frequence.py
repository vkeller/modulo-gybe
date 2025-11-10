import random
from collections import Counter

texte = "le renard le corbeau le fromage le arbre"
mots = texte.split()
freq = Counter(mots)

# Générer une phrase avec pondération
def generer_par_frequence(n=6):
    population = list(freq.keys())
    weights = list(freq.values())
    return " ".join(random.choices(population, weights=weights, k=n)) + "."

print(generer_par_frequence())