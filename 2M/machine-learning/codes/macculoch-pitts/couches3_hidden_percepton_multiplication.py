import random
import math

# ============================================
# 1. INITIALISATION STABLE
# ============================================
# Poids initialisés petits pour éviter l'explosion
w_c1 = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
b_c1 = random.uniform(-0.1, 0.1)

w_c2 = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
b_c2 = random.uniform(-0.1, 0.1)

w_out = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
b_out = random.uniform(-0.1, 0.1)

# Taux d'apprentissage PLUS PETIT pour plus de stabilité
taux_apprentissage = 0.001

# ============================================
# 2. DONNÉES NORMALISÉES (Important !)
# ============================================
# On divise par 20 pour avoir des entrées entre 0 et 1
# Ça aide énormément à stabiliser l'apprentissage
max_val = 20.0

donnees = []
for i in range(200):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    # On normalise les entrées ET la cible
    donnees.append((a / max_val, b / max_val, (a * b) / (max_val * max_val)))

print("=== APPRENTISSAGE MULTIPLICATION (RÉSEAU STABLE) ===\n")

# ============================================
# 3. ENTRAÎNEMENT AVEC SÉCURITÉ
# ============================================
for epoch in range(6000):
    erreur_totale = 0
    
    for a_norm, b_norm, cible_norm in donnees:
        
        # --- Phase Forward ---
        # Couche cachée 1
        somme_c1 = (a_norm * w_c1[0]) + (b_norm * w_c1[1]) + b_c1
        sortie_c1 = max(0, somme_c1)  # ReLU
        
        # Couche cachée 2
        somme_c2 = (a_norm * w_c2[0]) + (b_norm * w_c2[1]) + b_c2
        sortie_c2 = max(0, somme_c2)  # ReLU
        
        # Couche de sortie
        prediction = (sortie_c1 * w_out[0]) + (sortie_c2 * w_out[1]) + b_out
        
        # --- Calcul de l'erreur ---
        erreur = cible_norm - prediction
        erreur_totale += abs(erreur)
        
        # --- Phase Backward avec protection ---
        # On limite l'erreur maximale pour éviter l'explosion
        erreur = max(-1.0, min(1.0, erreur))
        
        # Mise à jour couche sortie
        w_out[0] += taux_apprentissage * erreur * sortie_c1
        w_out[1] += taux_apprentissage * erreur * sortie_c2
        b_out += taux_apprentissage * erreur
        
        # Mise à jour couche cachée
        if sortie_c1 > 0:
            erreur_c1 = erreur * w_out[0]
            erreur_c1 = max(-1.0, min(1.0, erreur_c1))  # Protection
            w_c1[0] += taux_apprentissage * erreur_c1 * a_norm
            w_c1[1] += taux_apprentissage * erreur_c1 * b_norm
            b_c1 += taux_apprentissage * erreur_c1
            
        if sortie_c2 > 0:
            erreur_c2 = erreur * w_out[1]
            erreur_c2 = max(-1.0, min(1.0, erreur_c2))  # Protection
            w_c2[0] += taux_apprentissage * erreur_c2 * a_norm
            w_c2[1] += taux_apprentissage * erreur_c2 * b_norm
            b_c2 += taux_apprentissage * erreur_c2
    
    # Vérification NaN
    if math.isnan(erreur_totale):
        print(f"ERREUR NaN détectée à l'époque {epoch} ! Arrêt.")
        break
    
    if epoch % 500 == 0:
        print(f"Époque {epoch} - Erreur: {erreur_totale:.4f}")

print("\n=== APPRENTISSAGE TERMINÉ ===\n")

# ============================================
# 4. TEST AVEC DÉNORMALISATION
# ============================================
tests = [(5, 5), (10, 3), (7, 8), (12, 10)]

print("=== TEST MULTIPLICATION ===\n")
for a, b in tests:
    # Normalisation des entrées
    a_norm = a / max_val
    b_norm = b / max_val
    
    # Calcul Forward
    somme_c1 = (a_norm * w_c1[0]) + (b_norm * w_c1[1]) + b_c1
    sortie_c1 = max(0, somme_c1)
    
    somme_c2 = (a_norm * w_c2[0]) + (b_norm * w_c2[1]) + b_c2
    sortie_c2 = max(0, somme_c2)
    
    prediction_norm = (sortie_c1 * w_out[0]) + (sortie_c2 * w_out[1]) + b_out
    
    # Dénormalisation du résultat (pour retrouver la vraie valeur)
    prediction = prediction_norm * (max_val * max_val)
    reel = a * b
    
    print(f"{a} × {b} = {prediction:.2f} (Réel: {reel}) - Écart: {abs(prediction-reel):.2f}")

print("\n✅ Si les écarts sont raisonnables, le réseau a appris !")