import random

# Paramètres
cible = "NSI GENIAL"
taille_population = 20
taux_mutation = 0.1
max_gen = 100

# Générer un individu aléatoire
def generer_individu():
    return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ") for _ in range(len(cible)))

# Calculer la fitness (nb de lettres correctes)
def fitness(individu):
    return sum(1 for a, b in zip(individu, cible) if a == b)

# Initialisation de la population
population = []
i = 0
while i < taille_population:
    population.append(generer_individu())
    i += 1

# Boucle évolutive
generation = 0
trouve = False
while generation < max_gen and not trouve:
    # Calculer les scores
    scores = []
    i = 0
    while i < len(population):
        scores.append((fitness(population[i]), population[i]))
        i += 1
    
    # Trier par score décroissant
    scores.sort(reverse=True)
    
    # Vérifier si on a trouvé la solution
    if scores[0][0] == len(cible):
        print("Trouvé en", generation, "générations :", scores[0][1])
        trouve = True
        break
    
    # Afficher le meilleur de la génération
    if generation % 10 == 0:
        print(f"Génération {generation} : {scores[0][1]} (score: {scores[0][0]})")
    
    # Sélectionner les parents (les 50% meilleurs)
    moitie = len(scores) // 2
    parents = []
    i = 0
    while i < moitie:
        parents.append(scores[i][1])
        i += 1
    
    # Créer nouvelle génération
    nouvelle_population = []
    while len(nouvelle_population) < taille_population:
        # Choisir deux parents au hasard
        p1 = random.choice(parents)
        p2 = random.choice(parents)
        
        # Croisement : alterner les lettres
        enfant = ""
        j = 0
        while j < len(cible):
            if random.random() < 0.5:
                enfant += p1[j]
            else:
                enfant += p2[j]
            j += 1
        
        # Mutation
        liste_enfant = list(enfant)
        j = 0
        while j < len(liste_enfant):
            if random.random() < taux_mutation:
                liste_enfant[j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
            j += 1
        enfant = ''.join(liste_enfant)
        
        nouvelle_population.append(enfant)
    
    population = nouvelle_population
    generation += 1

if not trouve:
    print("Pas trouvé. Meilleur :", scores[0][1], "avec score", scores[0][0])