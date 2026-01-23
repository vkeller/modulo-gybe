import random

# Paramètres
cible = "BONJOUR LAUSANNE"
taille_population = 300
taux_mutation = 0.15
max_gen = 1000

# Générer la population initiale (sans fonction)
population = []
i = 0
while i < taille_population:
    individu = ""
    j = 0
    while j < len(cible):
        # Lettres possibles : A-Z + espace
        individu += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        j += 1
    population.append(individu)
    i += 1

# Boucle principale
generation = 0
trouve = False
while generation < max_gen and not trouve:
    # Calculer les scores (fitness)
    scores = []
    i = 0
    while i < len(population):
        fit = 0
        k = 0
        while k < len(cible):
            if population[i][k] == cible[k]:
                fit += 1
            k += 1
        scores.append((fit, population[i]))
        i += 1
    
    # Trier manuellement (simplifié : on cherche le meilleur)
    # Pour la démo, on affiche juste le meilleur
    meilleur_score = -1
    meilleur_individu = ""
    i = 0
    while i < len(scores):
        if scores[i][0] > meilleur_score:
            meilleur_score = scores[i][0]
            meilleur_individu = scores[i][1]
        i += 1
    
    if meilleur_score == len(cible):
        print("Trouvé en", generation, "générations :", meilleur_individu)
        trouve = True
        break
    
    if generation % 5 == 0:
        print(f"G{generation}: {meilleur_individu} (score: {meilleur_score})")
    
    # Sélection : garder les individus avec score >= moyenne
    somme = 0
    i = 0
    while i < len(scores):
        somme += scores[i][0]
        i += 1
    moyenne = somme / len(scores)
    
    parents = []
    i = 0
    while i < len(scores):
        if scores[i][0] >= moyenne:
            parents.append(scores[i][1])
        i += 1
    
    # Si aucun parent, garder tous
    if len(parents) == 0:
        parents = population[:]
    
    # Créer nouvelle génération
    nouvelle_population = []
    while len(nouvelle_population) < taille_population:
        # Choisir deux parents au hasard
        p1 = parents[random.randint(0, len(parents)-1)]
        p2 = parents[random.randint(0, len(parents)-1)]
        
        # Croisement
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
    print("Pas trouvé. Meilleur :", meilleur_individu, "score =", meilleur_score)