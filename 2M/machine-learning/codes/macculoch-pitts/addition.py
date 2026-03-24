# 1. Définition des entrées possibles (Table de vérité)
# (Entrée A, Entrée B)
entrees = [(0, 0), (0, 1), (1, 0), (1, 1)]

# 2. Configuration du Neurone 1 : La Retenue (Logique ET)
# Il s'active seulement si A=1 ET B=1 (Somme des poids >= 2)
poids_n1_a = 1
poids_n1_b = 1
seuil_n1 = 2  # Seuil élevé pour exiger les deux entrées

# 3. Configuration du Neurone 2 : La Somme (Logique OU simplifiée)
# Il s'active si A=1 OU B=1 (Somme des poids >= 1)
poids_n2_a = 1
poids_n2_b = 1
seuil_n2 = 1  # Seuil bas pour s'activer avec une seule entrée

# 4. Affichage de l'en-tête
print("A | B || Retenue (ET) | Somme (OU)")
print("--|---||---------------|------------")

# 5. Boucle principale pour tester toutes les combinaisons
for a, b in entrees:
    # --- Calcul Neurone 1 (Retenue) ---
    activation_n1 = (a * poids_n1_a) + (b * poids_n1_b)
    if activation_n1 >= seuil_n1:
        sortie_n1 = 1
    else:
        sortie_n1 = 0

    # --- Calcul Neurone 2 (Somme) ---
    activation_n2 = (a * poids_n2_a) + (b * poids_n2_b)
    if activation_n2 >= seuil_n2:
        sortie_n2 = 1
    else:
        sortie_n2 = 0

    # --- Affichage du résultat ---
    print(f"{a} | {b} ||      {sortie_n1}        |      {sortie_n2}")

# 6. Explication finale
print("\nNote : Pour une addition binaire parfaite (1+1=10), la somme nécessite")
print("une logique XOR qui est impossible avec un seul neurone simple.")
print("Ici, le neurone 1 gère correctement la retenue (1+1 -> Retenue 1).")