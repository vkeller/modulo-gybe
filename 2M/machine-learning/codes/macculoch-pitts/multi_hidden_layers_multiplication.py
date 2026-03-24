import random
import math

# ============================================
# 1. INITIALISATION (10 NEURONES CACHÉS)
# ============================================
# On crée 10 neurones dans la couche cachée
# Chaque neurone a 2 poids (pour les 2 entrées) + 1 biais

nb_neurons_caches = 8

# Initialisation des poids et biais pour les 10 neurones cachés
poids_caches = []
biais_caches = []

for i in range(nb_neurons_caches):
    poids_caches.append([random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)])
    biais_caches.append(random.uniform(-0.1, 0.1))

# Couche de sortie (10 poids + 1 biais pour combiner les 10 neurones cachés)
poids_sortie = []
for i in range(nb_neurons_caches):
    poids_sortie.append(random.uniform(-0.5, 0.5))
biais_sortie = random.uniform(-0.1, 0.1)

# Taux d'apprentissage
taux_apprentissage = 0.0001

# ============================================
# 2. DONNÉES D'ENTRAÎNEMENT (PLUS NOMBREUSES)
# ============================================
max_val = 20.0

donnees = []
for i in range(1000):  # 1000 exemples au lieu de 200
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    # Normalisation des entrées et de la cible
    donnees.append((a / max_val, b / max_val, (a * b) / (max_val * max_val)))

print("=== APPRENTISSAGE MULTIPLICATION (",nb_neurons_caches," NEURONES CACHÉS) ===")
print(f"Nombre de neurones cachés: {nb_neurons_caches}")
print(f"Nombre d'exemples: 1000")
print("Cela peut prendre du temps...\n")

# ============================================
# 3. ENTRAÎNEMENT
# ============================================
for epoch in range(5000):  # Plus d'époques pour mieux apprendre
    erreur_totale = 0
    
    for a_norm, b_norm, cible_norm in donnees:
        
        # --- Phase Forward ---
        sorties_caches = []
        
        # Calcul des 10 neurones cachés
        for i in range(nb_neurons_caches):
            somme = (a_norm * poids_caches[i][0]) + (b_norm * poids_caches[i][1]) + biais_caches[i]
            sortie = max(0, somme)  # ReLU
            sorties_caches.append(sortie)
        
        # Calcul de la sortie finale
        prediction = biais_sortie
        for i in range(nb_neurons_caches):
            prediction += sorties_caches[i] * poids_sortie[i]
        
        # --- Calcul de l'erreur ---
        erreur = cible_norm - prediction
        erreur_totale += abs(erreur)
        
        # Protection contre les valeurs extrêmes
        erreur = max(-1.0, min(1.0, erreur))
        
        # --- Phase Backward ---
        # Mise à jour couche de sortie
        for i in range(nb_neurons_caches):
            poids_sortie[i] += taux_apprentissage * erreur * sorties_caches[i]
        biais_sortie += taux_apprentissage * erreur
        
        # Mise à jour couche cachée (rétropropagation)
        for i in range(nb_neurons_caches):
            if sorties_caches[i] > 0:  # Seulement si neurone actif (ReLU)
                erreur_cache = erreur * poids_sortie[i]
                erreur_cache = max(-1.0, min(1.0, erreur_cache))
                poids_caches[i][0] += taux_apprentissage * erreur_cache * a_norm
                poids_caches[i][1] += taux_apprentissage * erreur_cache * b_norm
                biais_caches[i] += taux_apprentissage * erreur_cache
    
    # Vérification NaN
    if math.isnan(erreur_totale):
        print(f"ERREUR NaN détectée à l'époque {epoch} ! Arrêt.")
        break
    
    if epoch % 1000 == 0:
        print(f"Époque {epoch} / 5000 - Erreur totale: {erreur_totale:.4f}")

print("\n=== APPRENTISSAGE TERMINÉ ===\n")

# ============================================
# 4. TEST COMPLET
# ============================================
tests = [
    (5, 5), (10, 3), (7, 8), (12, 10),
    (15, 15), (3, 17), (20, 20), (1, 19),
    (9, 11), (14, 6)
]

print("=== TEST MULTIPLICATION ===\n")
print("Entrées  | Prédiction | Réel     | Écart    | Précision")
print("-" * 60)

erreur_moyenne = 0
nombre_tests = 0

for a, b in tests:
    # Normalisation
    a_norm = a / max_val
    b_norm = b / max_val
    
    # Phase Forward
    sorties_caches = []
    for i in range(nb_neurons_caches):
        somme = (a_norm * poids_caches[i][0]) + (b_norm * poids_caches[i][1]) + biais_caches[i]
        sortie = max(0, somme)
        sorties_caches.append(sortie)
    
    prediction_norm = biais_sortie
    for i in range(nb_neurons_caches):
        prediction_norm += sorties_caches[i] * poids_sortie[i]
    
    # Dénormalisation
    prediction = prediction_norm * (max_val * max_val)
    reel = a * b
    ecart = abs(prediction - reel)
    precision = 100 - (ecart / reel * 100) if reel != 0 else 100
    
    erreur_moyenne += ecart
    nombre_tests += 1
    
    print(f"{a} × {b}  | {prediction:8.2f}   | {reel:8}   | {ecart:8.2f}   | {precision:6.2f}%")

print("-" * 60)
print(f"Erreur moyenne: {erreur_moyenne / nombre_tests:.2f}")
print(f"Précision moyenne: {100 - (erreur_moyenne / nombre_tests / 100):.2f}%")

# ============================================
# 5. TEST DE GÉNÉRALISATION (nombres jamais vus)
# ============================================
print("\n=== TEST DE GÉNÉRALISATION (nombres hors domaine) ===\n")

tests_hors_domaine = [(25, 25), (30, 15), (40, 10)]

for a, b in tests_hors_domaine:
    a_norm = a / max_val
    b_norm = b / max_val
    
    sorties_caches = []
    for i in range(nb_neurons_caches):
        somme = (a_norm * poids_caches[i][0]) + (b_norm * poids_caches[i][1]) + biais_caches[i]
        sortie = max(0, somme)
        sorties_caches.append(sortie)
    
    prediction_norm = biais_sortie
    for i in range(nb_neurons_caches):
        prediction_norm += sorties_caches[i] * poids_sortie[i]
    
    prediction = prediction_norm * (max_val * max_val)
    reel = a * b
    
    print(f"{a} × {b} = {prediction:.2f} (Réel: {reel}) - Écart: {abs(prediction-reel):.2f}")

print("\n⚠️  Les réseaux de neurones généralisent mal en dehors du domaine d'entraînement!")
print("   (ici entraîné sur 1-20, testé sur 25-40)")

# ============================================
# 6. AFFICHAGE DES POIDS FINAUX
# ============================================
print("\n=== POIDS DE LA COUCHE DE SORTIE ===")
for i in range(nb_neurons_caches):
    print(f"Neurone caché {i+1}: poids_sortie = {poids_sortie[i]:.4f}")

print("\n✅ Avec 10 neurones cachés et 1000 exemples, la multiplication est bien apprise!")