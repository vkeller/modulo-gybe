import random

# ============================================================
# 1. FONCTION DE FITNESS
# ============================================================
def fitness(chromosome):
    """
    Évalue la qualité d'un individu.
    Objectif : avoir AU MAXIMUM un seul '1'.
    - 0 ou 1 bit à 1 → fitness = 100 (optimal)
    - 2 bits à 1 → fitness = 99
    - 3 bits à 1 → fitness = 96, etc.
    """
    nb_uns = sum(chromosome)
    return nb_uns
#    if nb_uns <= 1:
#        return 100
#    else:
#        return 100 - (nb_uns - 1) ** 2


# ============================================================
# 2. INITIALISATION
# ============================================================
def creer_individu(taille):
    """Crée un individu aléatoire (liste de 0 et 1)"""
    return [random.randint(0, 1) for _ in range(taille)]

def creer_population(taille_pop, taille_individu):
    """Crée une population complète"""
    return [creer_individu(taille_individu) for _ in range(taille_pop)]


# ============================================================
# 3. SÉLECTION PAR TOURNOI
# ============================================================
def selection_tournoi(population, fitnesses, k=3):
    """
    Sélection robuste :
    - Choisit k individus au hasard
    - Retourne une COPIE du meilleur
    """
    # Gestion sécurisée si k > taille population
    k_eff = min(k, len(population))
    participants = random.sample(range(len(population)), k_eff)
    meilleur_idx = max(participants, key=lambda i: fitnesses[i])
    return population[meilleur_idx][:]  # [:] = copie indispensable !


# ============================================================
# 4. OPÉRATEURS GÉNÉTIQUES (CORRIGÉS)
# ============================================================
def croisement(parent1, parent2, taux_croisement=0.8):
    """Croisement à un point avec probabilité"""
    if random.random() < taux_croisement:
        point = random.randint(1, len(parent1) - 1)
        enfant1 = parent1[:point] + parent2[point:]
        enfant2 = parent2[:point] + parent1[point:]
        return enfant1, enfant2
    else:
        # Toujours retourner des COPIES
        return parent1[:], parent2[:]

def mutation(individu, taux_mutation=0.05):
    """
    CORRECTION CRITIQUE :
    - Ne JAMAIS modifier l'original → créer une copie d'abord
    - Évite la contamination des parents dans la population
    """
    resultat = individu[:]  # Copie sécurisée
    for i in range(len(resultat)):
        if random.random() < taux_mutation:
            resultat[i] = 1 - resultat[i]  # Inversion 0↔1
    return resultat


# ============================================================
# 5. ALGORITHME GÉNÉTIQUE PRINCIPAL (CORRIGÉ)
# ============================================================
def algorithme_genetique(taille_individu=8, taille_pop=20, generations=30):
    # Initialisation
    population = creer_population(taille_pop, taille_individu)
    
    print("="*60)
    print("ALGORITHME GÉNÉTIQUE : Chaîne avec ≤1 bit à 1")
    print("="*60)
    print(f"Taille chromosome : {taille_individu} bits")
    print(f"Taille population : {taille_pop} individus")
    print(f"Nombre générations : {generations}")
    print("="*60 + "\n")
    
    for gen in range(generations):
        # Calcul des fitness
        fitnesses = [fitness(ind) for ind in population]
        
        # Meilleur individu de la génération
        meilleur_idx = max(range(len(population)), key=lambda i: fitnesses[i])
        meilleur_ind = population[meilleur_idx]
        meilleure_fit = fitnesses[meilleur_idx]
        nb_uns = sum(meilleur_ind)
        
        # Affichage périodique
        if gen % 5 == 0 or gen == generations - 1 or meilleure_fit == 100:
            chaine = ''.join(map(str, meilleur_ind))
            print(f"Génération {gen:2d} | Meilleur : {chaine} "
                  f"(nb 1 = {nb_uns}, fitness = {meilleure_fit})")
        
        # Arrêt prématuré si solution optimale
        if meilleure_fit == 100 and nb_uns <= 1:
            print("\n✅ SOLUTION OPTIMALE TROUVÉE !")
            return meilleur_ind[:]
        
        # ------------------------------
        # Création de la NOUVELLE génération (CORRIGÉ)
        # ------------------------------
        nouvelle_pop = []
        
        # 1. ÉLITISME : sauvegarder le champion (copie !)
        nouvelle_pop.append(meilleur_ind[:])
        
        # 2. Reproduction jusqu'à remplir la population
        while len(nouvelle_pop) < taille_pop:
            # Sélection de parents (copies garanties par selection_tournoi)
            parent1 = selection_tournoi(population, fitnesses)
            parent2 = selection_tournoi(population, fitnesses)
            
            # Croisement → renvoie des copies
            enfant1, enfant2 = croisement(parent1, parent2)
            
            # Mutation → renvoie de NOUVELLES copies
            enfant1 = mutation(enfant1)
            enfant2 = mutation(enfant2)
            
            # Ajout sécurisé
            nouvelle_pop.append(enfant1)
            if len(nouvelle_pop) < taille_pop:
                nouvelle_pop.append(enfant2)
        
        # Remplacer l'ancienne population
        population = nouvelle_pop
    
    # Retourner le meilleur de la dernière génération
    fitnesses = [fitness(ind) for ind in population]
    meilleur_idx = max(range(len(population)), key=lambda i: fitnesses[i])
    meilleur_ind = population[meilleur_idx]
    print("\n⚠️  Fin des générations — meilleure solution trouvée :")
    return meilleur_ind[:]


# ============================================================
# 6. EXÉCUTION
# ============================================================
if __name__ == "__main__":
    random.seed(42)  # Reproductibilité pour la démo en classe
    solution = algorithme_genetique(taille_individu=16, taille_pop=20, generations=30)
    print("\n" + "="*60)
    print("📋 SOLUTION FINALE :", ''.join(map(str, solution)))
    print("   Nombre de bits à '1' :", sum(solution))
    print("="*60)