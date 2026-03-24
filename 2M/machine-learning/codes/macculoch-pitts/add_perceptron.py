# 1. Les entrées (nombres entiers décimaux)
entree_1 = 5
entree_2 = 7

# 2. Les poids (On met 1 pour que le poids n'change pas la valeur)
poids_1 = 1
poids_2 = 1

# 3. Le Biais (Souvent utilisé dans les Perceptrons, ici on le met à 0)
biais = 0

# 4. Calcul de la sortie (Somme pondérée)
# C'est la formule de base d'un neurone : (Entrée * Poids) + Biais
# On ne met PAS de seuil ici, sinon on perdrait le nombre exact.
resultat = (entree_1 * poids_1) + (entree_2 * poids_2) + biais

# 5. Affichage
print("--- Calcul par le Neurone Linéaire ---")
print(f"Entrées : {entree_1} et {entree_2}")
print(f"Poids   : {poids_1} et {poids_2}")
print(f"Résultat de l'addition : {resultat}")

# 6. Comparaison avec un neurone classique (McCulloch-Pitts)
seuil = 10
if resultat >= seuil:
    sortie_binaire = 1
else:
    sortie_binaire = 0

print(f"\nSi on ajoutait un seuil de {seuil} (McCulloch-Pitts), la sortie serait : {sortie_binaire}")
print("C'est pour cela qu'on retire le seuil pour faire des calculs mathématiques.")