import random

# -----------------------------
# Paramètres du problème
# -----------------------------

# Matrice de distances (symétrique, diagonale nulle)
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

NB_VILLES = len(distances)
TAILLE_POPULATION = 20
NB_GENERATIONS = 100
TAUX_CROISEMENT = 0.2
TAUX_MUTATION = 0.05


# -----------------------------
# Fonctions utilitaires
# -----------------------------

def creer_individu():
    """Crée un individu : permutation aléatoire des villes."""
    individu = list(range(NB_VILLES))
    random.shuffle(individu)
    return individu

def creer_population():
    """Crée une population initiale."""
    return [creer_individu() for _ in range(TAILLE_POPULATION)]

def calculer_distance(individu):
    """Calcule la distance totale du trajet (fermé)."""
    dist = 0
    for i in range(len(individu)):
        ville_actuelle = individu[i]
        ville_suivante = individu[(i + 1) % NB_VILLES]  # retour à la première à la fin
        dist += distances[ville_actuelle][ville_suivante]
    return dist

def fitness(individu):
    """Fonction de fitness : plus la distance est petite, plus le score est grand."""
    return 1 / (1 + calculer_distance(individu))

def selection_roulette(population, fitnesses):
    """Sélection par roulette."""
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitnesses):
        current += f
        if current >= pick:
            return population[i]

def croisement(parent1, parent2):
    """Croisement par ordre (Order Crossover - OX)."""
    taille = len(parent1)
    debut, fin = sorted(random.sample(range(taille), 2))

    # Enfant commence vide
    enfant = [-1] * taille

    # Copier la tranche de parent1
    for i in range(debut, fin):
        enfant[i] = parent1[i]

    # Remplir le reste avec l'ordre de parent2
    ptr = 0
    for i in range(taille):
        if enfant[i] == -1:
            while parent2[ptr] in enfant:
                ptr += 1
            enfant[i] = parent2[ptr]
            ptr += 1

    return enfant

def mutation(individu, taux):
    """Mutation par échange de deux villes (swap), appliquée avec probabilité 'taux'."""
    if random.random() < taux:
        i, j = random.sample(range(len(individu)), 2)
        individu[i], individu[j] = individu[j], individu[i]
    return individu

# -----------------------------
# Algorithme génétique principal
# -----------------------------

def algorithme_genetique():
    population = creer_population()

    for generation in range(NB_GENERATIONS):
        # Calcul des fitness
        fitnesses = [fitness(ind) for ind in population]

        # Meilleur individu de la génération
        meilleur_indice = fitnesses.index(max(fitnesses))
        meilleur = population[meilleur_indice]
        meilleure_distance = calculer_distance(meilleur)

        print(f"Génération {generation:3d} | Meilleure distance : {meilleure_distance}")

        # Créer nouvelle population
        nouvelle_population = []
        while len(nouvelle_population) < TAILLE_POPULATION:
            parent1 = selection_roulette(population, fitnesses)
            parent2 = selection_roulette(population, fitnesses)

            if random.random() < TAUX_CROISEMENT:
                enfant1 = croisement(parent1[:], parent2[:])
                enfant2 = croisement(parent2[:], parent1[:])
            else:
                enfant1, enfant2 = parent1[:], parent2[:]

            enfant1 = mutation(enfant1, TAUX_MUTATION)
            enfant2 = mutation(enfant2, TAUX_MUTATION)

            nouvelle_population.append(enfant1)
            if len(nouvelle_population) < TAILLE_POPULATION:
                nouvelle_population.append(enfant2)

        population = nouvelle_population

    # Retourner le meilleur trouvé
    fitnesses = [fitness(ind) for ind in population]
    meilleur_indice = fitnesses.index(max(fitnesses))
    meilleur = population[meilleur_indice]
    return meilleur, calculer_distance(meilleur)

# -----------------------------
# Lancement
# -----------------------------

if __name__ == "__main__":
    solution, distance = algorithme_genetique()
    print("\n✅ Meilleure solution trouvée :", solution)
    print("📏 Distance totale :", distance)