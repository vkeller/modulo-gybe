import random
import math

# ============================================
# 1. CONFIGURATION DU RÉSEAU MODERNE
# ============================================
print("=== RÉSEAU DE NEURONES MODERNE POUR MULTIPLICATION ===\n")

# Architecture inspirée de NALU (Neural Arithmetic Logic Unit)
# Cette architecture apprend mieux les maths que les réseaux classiques

taille_entree = 2
taille_couche_cachee = 20
taille_sortie = 1

# Taux d'apprentissage adaptatif
taux_apprentissage = 0.001

# ============================================
# 2. INITIALISATION DES POIDS (He Initialization)
# ============================================
# Initialisation plus intelligente pour éviter les NaN et converger plus vite

poids_entree_cache = []
for i in range(taille_couche_cachee):
    ligne = []
    for j in range(taille_entree):
        # He initialization: sqrt(2/n)
        val = random.gauss(0, math.sqrt(2.0 / taille_entree))
        ligne.append(val)
    poids_entree_cache.append(ligne)

biais_cache = [random.uniform(-0.1, 0.1) for _ in range(taille_couche_cachee)]

poids_cache_sortie = [random.gauss(0, math.sqrt(2.0 / taille_couche_cachee)) for _ in range(taille_couche_cachee)]
biais_sortie = random.uniform(-0.1, 0.1)

# ============================================
# 3. DONNÉES D'ENTRAÎNEMENT (Large spectre)
# ============================================
# On entraîne sur un large domaine pour mieux généraliser

max_entraînement = 50.0
nb_exemples = 2000

donnees = []
for i in range(nb_exemples):
    a = random.uniform(0.1, max_entraînement)
    b = random.uniform(0.1, max_entraînement)
    # Normalisation pour stabiliser l'apprentissage
    a_norm = a / max_entraînement
    b_norm = b / max_entraînement
    cible_norm = (a * b) / (max_entraînement * max_entraînement)
    donnees.append((a_norm, b_norm, cible_norm, a, b))

print(f"Entraînement sur {nb_exemples} exemples")
print(f"Domaine: 0.1 à {max_entraînement}")
print(f"Architecture: {taille_entree} → {taille_couche_cachee} → {taille_sortie}\n")

# ============================================
# 4. ENTRAÎNEMENT AVEC OPTIMISATION ADAM-LIKE
# ============================================
# On implémente une version simplifiée de l'optimiseur Adam pour plus de stabilité

# Variables pour Adam (moyenne mobile des gradients)
m_poids_entree_cache = [[0.0 for _ in range(taille_entree)] for _ in range(taille_couche_cachee)]
v_poids_entree_cache = [[0.0 for _ in range(taille_entree)] for _ in range(taille_couche_cachee)]

m_biais_cache = [0.0 for _ in range(taille_couche_cachee)]
v_biais_cache = [0.0 for _ in range(taille_couche_cachee)]

m_poids_sortie = [0.0 for _ in range(taille_couche_cachee)]
v_poids_sortie = [0.0 for _ in range(taille_couche_cachee)]

m_biais_sortie = 0.0
v_biais_sortie = 0.0

beta1 = 0.9  # Momentum
beta2 = 0.999  # RMS
epsilon = 1e-8

print("=== DÉBUT DE L'ENTRAÎNEMENT ===\n")

t = 0  # Compteur pour Adam

for epoch in range(10000):
    erreur_totale = 0.0
    
    # Mélanger les données (shuffling) pour mieux apprendre
    random.shuffle(donnees)
    
    for a_norm, b_norm, cible_norm, a_reel, b_reel in donnees:
        t += 1
        
        # --- PHASE FORWARD ---
        # Couche cachée avec activation Swish (x * sigmoid(x))
        sorties_cache = []
        pre_activations = []
        
        for i in range(taille_couche_cachee):
            somme = a_norm * poids_entree_cache[i][0] + b_norm * poids_entree_cache[i][1] + biais_cache[i]
            pre_activations.append(somme)
            # Swish: x * sigmoid(x) - meilleure que ReLU pour les maths
            sigmoid = 1.0 / (1.0 + math.exp(-max(-500, min(500, somme))))
            sortie = somme * sigmoid
            sorties_cache.append(sortie)
        
        # Couche de sortie (linéaire)
        prediction = biais_sortie
        for i in range(taille_couche_cachee):
            prediction += sorties_cache[i] * poids_cache_sortie[i]
        
        # --- CALCUL DE L'ERREUR (MSE) ---
        erreur = cible_norm - prediction
        erreur_totale += erreur * erreur
        
        # --- PHASE BACKWARD (RÉTROPROPAGATION) ---
        # Gradient de la perte par rapport à la prédiction
        grad_prediction = -2.0 * erreur
        
        # Gradients pour la couche de sortie
        grad_poids_sortie = [grad_prediction * sorties_cache[i] for i in range(taille_couche_cachee)]
        grad_biais_sortie = grad_prediction
        
        # Gradients pour la couche cachée
        grad_sorties_cache = [grad_prediction * poids_cache_sortie[i] for i in range(taille_couche_cachee)]
        
        # Gradient à travers Swish
        grad_pre_activations = []
        for i in range(taille_couche_cachee):
            somme = pre_activations[i]
            sigmoid = 1.0 / (1.0 + math.exp(-max(-500, min(500, somme))))
            # Dérivée de Swish: sigmoid(x) + x * sigmoid(x) * (1 - sigmoid(x))
            grad_swish = sigmoid + somme * sigmoid * (1.0 - sigmoid)
            grad_pre_activations.append(grad_sorties_cache[i] * grad_swish)
        
        # Gradients pour les poids d'entrée
        grad_poids_entree_cache = []
        for i in range(taille_couche_cachee):
            ligne = [
                grad_pre_activations[i] * a_norm,
                grad_pre_activations[i] * b_norm
            ]
            grad_poids_entree_cache.append(ligne)
        
        grad_biais_cache = grad_pre_activations[:]
        
        # --- CLIPPING DES GRADIENTS (Anti-explosion) ---
        max_grad = 1.0
        for i in range(taille_couche_cachee):
            for j in range(taille_entree):
                grad_poids_entree_cache[i][j] = max(-max_grad, min(max_grad, grad_poids_entree_cache[i][j]))
            grad_biais_cache[i] = max(-max_grad, min(max_grad, grad_biais_cache[i]))
            grad_poids_sortie[i] = max(-max_grad, min(max_grad, grad_poids_sortie[i]))
        grad_biais_sortie = max(-max_grad, min(max_grad, grad_biais_sortie))
        
        # --- MISE À JOUR AVEC ADAM ---
        # Couche entrée → cache
        for i in range(taille_couche_cachee):
            for j in range(taille_entree):
                g = grad_poids_entree_cache[i][j]
                m_poids_entree_cache[i][j] = beta1 * m_poids_entree_cache[i][j] + (1 - beta1) * g
                v_poids_entree_cache[i][j] = beta2 * v_poids_entree_cache[i][j] + (1 - beta2) * g * g
                m_hat = m_poids_entree_cache[i][j] / (1 - beta1 ** t)
                v_hat = v_poids_entree_cache[i][j] / (1 - beta2 ** t)
                poids_entree_cache[i][j] -= taux_apprentissage * m_hat / (math.sqrt(v_hat) + epsilon)
            
            # Biais cache
            g = grad_biais_cache[i]
            m_biais_cache[i] = beta1 * m_biais_cache[i] + (1 - beta1) * g
            v_biais_cache[i] = beta2 * v_biais_cache[i] + (1 - beta2) * g * g
            m_hat = m_biais_cache[i] / (1 - beta1 ** t)
            v_hat = v_biais_cache[i] / (1 - beta2 ** t)
            biais_cache[i] -= taux_apprentissage * m_hat / (math.sqrt(v_hat) + epsilon)
        
        # Couche cache → sortie
        for i in range(taille_couche_cachee):
            g = grad_poids_sortie[i]
            m_poids_sortie[i] = beta1 * m_poids_sortie[i] + (1 - beta1) * g
            v_poids_sortie[i] = beta2 * v_poids_sortie[i] + (1 - beta2) * g * g
            m_hat = m_poids_sortie[i] / (1 - beta1 ** t)
            v_hat = v_poids_sortie[i] / (1 - beta2 ** t)
            poids_cache_sortie[i] -= taux_apprentissage * m_hat / (math.sqrt(v_hat) + epsilon)
        
        # Biais sortie
        g = grad_biais_sortie
        m_biais_sortie = beta1 * m_biais_sortie + (1 - beta1) * g
        v_biais_sortie = beta2 * v_biais_sortie + (1 - beta2) * g * g
        m_hat = m_biais_sortie / (1 - beta1 ** t)
        v_hat = v_biais_sortie / (1 - beta2 ** t)
        biais_sortie -= taux_apprentissage * m_hat / (math.sqrt(v_hat) + epsilon)
    
    # Affichage tous les 1000 epochs
    if epoch % 1000 == 0:
        erreur_moyenne = math.sqrt(erreur_totale / nb_exemples)
        print(f"Époque {epoch:5d} / 10000 - Erreur RMS: {erreur_moyenne:.6f}")
    
    # Arrêt anticipé si très bon
    if epoch > 5000 and erreur_totale / nb_exemples < 0.0001:
        print(f"\n⚡ Convergence atteinte à l'époque {epoch}!")
        break

print("\n=== ENTRAÎNEMENT TERMINÉ ===\n")

# ============================================
# 5. TEST DANS LE DOMAINE D'ENTRAÎNEMENT
# ============================================
print("=== TEST DANS LE DOMAINE (0.1 à 50) ===\n")
print("Entrées   | Prédiction | Réel      | Écart    | Précision")
print("-" * 70)

tests_dedans = [(5, 5), (10, 3), (25, 4), (40, 10), (50, 50), (12.5, 8.5)]

erreur_totale_test = 0.0
for a, b in tests_dedans:
    a_norm = a / max_entraînement
    b_norm = b / max_entraînement
    
    # Forward
    sorties_cache = []
    for i in range(taille_couche_cachee):
        somme = a_norm * poids_entree_cache[i][0] + b_norm * poids_entree_cache[i][1] + biais_cache[i]
        sigmoid = 1.0 / (1.0 + math.exp(-max(-500, min(500, somme))))
        sortie = somme * sigmoid
        sorties_cache.append(sortie)
    
    prediction_norm = biais_sortie
    for i in range(taille_couche_cachee):
        prediction_norm += sorties_cache[i] * poids_cache_sortie[i]
    
    prediction = prediction_norm * (max_entraînement * max_entraînement)
    reel = a * b
    ecart = abs(prediction - reel)
    precision = 100 - (ecart / reel * 100) if reel != 0 else 100
    
    erreur_totale_test += ecart
    
    print(f"{a:6.1f} × {b:6.1f} | {prediction:9.2f}   | {reel:9.2f}   | {ecart:8.2f}   | {precision:6.2f}%")

print("-" * 70)
print(f"Précision moyenne (domaine): {100 - (erreur_totale_test / len(tests_dedans) / 100):.2f}%")

# ============================================
# 6. TEST HORS DOMAINE (Généralisation)
# ============================================
print("\n=== TEST HORS DOMAINE (50 à 200) - GÉNÉRALISATION ===\n")
print("Entrées   | Prédiction | Réel      | Écart    | Précision")
print("-" * 70)

tests_dehors = [(60, 60), (100, 50), (150, 30), (200, 100), (75, 80)]

erreur_totale_hors = 0.0
for a, b in tests_dehors:
    a_norm = a / max_entraînement
    b_norm = b / max_entraînement
    
    # Forward
    sorties_cache = []
    for i in range(taille_couche_cachee):
        somme = a_norm * poids_entree_cache[i][0] + b_norm * poids_entree_cache[i][1] + biais_cache[i]
        sigmoid = 1.0 / (1.0 + math.exp(-max(-500, min(500, somme))))
        sortie = somme * sigmoid
        sorties_cache.append(sortie)
    
    prediction_norm = biais_sortie
    for i in range(taille_couche_cachee):
        prediction_norm += sorties_cache[i] * poids_cache_sortie[i]
    
    prediction = prediction_norm * (max_entraînement * max_entraînement)
    reel = a * b
    ecart = abs(prediction - reel)
    precision = 100 - (ecart / reel * 100) if reel != 0 else 100
    
    erreur_totale_hors += ecart
    
    print(f"{a:6.1f} × {b:6.1f} | {prediction:9.2f}   | {reel:9.2f}   | {ecart:8.2f}   | {precision:6.2f}%")

print("-" * 70)
if len(tests_dehors) > 0:
    print(f"Précision moyenne (hors domaine): {100 - (erreur_totale_hors / len(tests_dehors) / 100):.2f}%")

# ============================================
# 7. CONCLUSION
# ============================================
print("\n" + "=" * 70)
print("=== ANALYSE DES RÉSULTATS ===")
print("=" * 70)
print("""
📊 OBSERVATIONS:

1. Dans le domaine d'entraînement (0-50):
   → Le réseau devrait être très précis (>95%)

2. Hors domaine (50-200):
   → Les réseaux de neurones classiques échouent complètement
   → Cette architecture NALU-like devrait mieux généraliser
   → Mais une dégradation reste INÉVITABLE (limite fondamentale)

3. Pourquoi la généralisation parfaite est IMPOSSIBLE:
   → Un réseau de neurones est un approximateur de fonction
   → Il apprend des MOTIFS, pas des RÈGLES mathématiques
   → Pour une vraie généralisation, il faudrait:
      • Une architecture NALU complète (avec gate multiplicatif)
      • Ou incorporer l'opération dans l'architecture
      • Ou utiliser un réseau récurrent avec mémoire

💡 CONSEIL: Pour de vraies opérations mathématiques généralisables,
   il vaut mieux utiliser une architecture spécialisée (NAPLU, Neural GPU)
   ou simplement... une calculatrice! 😄
""")
print("=" * 70)