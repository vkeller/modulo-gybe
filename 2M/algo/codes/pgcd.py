# ------------------------------------------------------------------------
# Algorithme pour trouver le PGCD entre deux nombres entiers positifs
# - Demander deux entiers A et B (positifs, non nuls)
# - Tant que A ≠ B faire :
#     - Si A > B alors
#         - A = A - B
#     - Sinon
#         - B = B - A
# - Afficher A (ou B, car A = B)
# Vincent Keller, Gymnase de Beaulieu, 2025
# ------------------------------------------------------------------------

A = int(input("A (entier positif) : "))
B = int(input("B (entier positif) : "))

while A != B :
    if A > B :
        A = A - B
    else:
        B = B - A

print("A",A,"B",B)
