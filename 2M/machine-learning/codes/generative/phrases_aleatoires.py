import random

sujets = ["Le chat", "Le robot", "L'IA", "Mon prof"]
verbes = ["mange", "écrit", "dessine", "rêve de"]
complements = ["une pomme", "un poème", "un cercle", "l'avenir"]

for _ in range(5):
    phrase = random.choice(sujets) + " " + random.choice(verbes) + " " + random.choice(complements) + "."
    print(phrase)