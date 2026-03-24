import random

# ============================================
# 1. INITIALISATION DES 4 PERCEPTRONS
# ============================================
# Chaque perceptron a 2 poids (w1, w2) et 1 biais (b)
# On initialise avec des nombres aléatoires entre 0 et 1

poids_add = [random.random(), random.random()]
biais_add = random.random()

poids_sub = [random.random(), random.random()]
biais_sub = random.random()

poids_mul = [random.random(), random.random()]
biais_mul = random.random()

poids_div = [random.random(), random.random()]
biais_div = random.random()

# Taux d'apprentissage (vitesse de correction des erreurs)
taux_apprentissage = 0.001

# ============================================
# 2. GÉNÉRATION DES DONNÉES D'ENTRAÎNEMENT
# ============================================
donnees = []
for i in range(200):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    donnees.append((a, b))

print("=== DÉBUT DE L'APPRENTISSAGE ===")
print("Cela peut prendre quelques secondes...\n")

# ============================================
# 3. BOUCLE D'APPRENTISSAGE (ENTRAÎNEMENT)
# ============================================
# On répète l'apprentissage 1000 fois sur toutes les données
for epoch in range(1000):
    
    # On parcourt toutes les paires de nombres
    for a, b in donnees:
        
        # --- PERCEPTRON 1 : ADDITION ---
        pred_add = (a * poids_add[0]) + (b * poids_add[1]) + biais_add
        cible_add = a + b
        erreur_add = cible_add - pred_add
        # Mise à jour des poids (Règle de Hebb / Delta)
        poids_add[0] += taux_apprentissage * erreur_add * a
        poids_add[1] += taux_apprentissage * erreur_add * b
        biais_add += taux_apprentissage * erreur_add

        # --- PERCEPTRON 2 : SOUSTRACTION ---
        pred_sub = (a * poids_sub[0]) + (b * poids_sub[1]) + biais_sub
        cible_sub = a - b
        erreur_sub = cible_sub - pred_sub
        poids_sub[0] += taux_apprentissage * erreur_sub * a
        poids_sub[1] += taux_apprentissage * erreur_sub * b
        biais_sub += taux_apprentissage * erreur_sub

        # --- PERCEPTRON 3 : MULTIPLICATION ---
        # (Attention : résultat approximatif car non-linéaire)
        pred_mul = (a * poids_mul[0]) + (b * poids_mul[1]) + biais_mul
        cible_mul = a * b
        erreur_mul = cible_mul - pred_mul
        poids_mul[0] += taux_apprentissage * erreur_mul * a
        poids_mul[1] += taux_apprentissage * erreur_mul * b
        biais_mul += taux_apprentissage * erreur_mul

        # --- PERCEPTRON 4 : DIVISION ---
        # (Attention : résultat approximatif car non-linéaire)
        if b != 0:
            pred_div = (a * poids_div[0]) + (b * poids_div[1]) + biais_div
            cible_div = a / b
            erreur_div = cible_div - pred_div
            poids_div[0] += taux_apprentissage * erreur_div * a
            poids_div[1] += taux_apprentissage * erreur_div * b
            biais_div += taux_apprentissage * erreur_div

    # Affichage de l'avancement tous les 200 cycles
    if epoch % 200 == 0:
        print(f"Cycle d'apprentissage {epoch} / 1000 terminé.")

print("\n=== APPRENTISSAGE TERMINÉ ===\n")

# ============================================
# 4. PHASE DE TEST (VÉRIFICATION)
# ============================================
tests = [(10, 5), (20, 4), (3, 7), (50, 10)]

print("=== RÉSULTATS SUR DE NOUVELLES DONNÉES ===\n")

for a, b in tests:
    print(f"Entrées : {a} et {b}")
    
    # Test Addition
    res_add = (a * poids_add[0]) + (b * poids_add[1]) + biais_add
    print(f"  Addition      : Calculé = {res_add:.2f} | Réel = {a + b}")
    
    # Test Soustraction
    res_sub = (a * poids_sub[0]) + (b * poids_sub[1]) + biais_sub
    print(f"  Soustraction  : Calculé = {res_sub:.2f} | Réel = {a - b}")
    
    # Test Multiplication
    res_mul = (a * poids_mul[0]) + (b * poids_mul[1]) + biais_mul
    print(f"  Multiplication: Calculé = {res_mul:.2f} | Réel = {a * b} (Approx)")
    
    # Test Division
    if b != 0:
        res_div = (a * poids_div[0]) + (b * poids_div[1]) + biais_div
        print(f"  Division      : Calculé = {res_div:.2f} | Réel = {a / b:.2f} (Approx)")
    
    print("")

# ============================================
# 5. AFFICHAGE DES POIDS FINAUX
# ============================================
print("=== POIDS APPRIS (PARAMÈTRES INTERNES) ===")
print(f"Addition      : w={poids_add}, b={biais_add:.2f}")
print(f"Soustraction  : w={poids_sub}, b={biais_sub:.2f}")
print(f"Multiplication: w={poids_mul}, b={biais_mul:.2f}")
print(f"Division      : w={poids_div}, b={biais_div:.2f}")
print("\nPour l'addition, les poids devraient être proches de [1.0, 1.0] et le biais proche de 0.0")