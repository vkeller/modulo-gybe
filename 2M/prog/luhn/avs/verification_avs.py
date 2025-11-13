# ================================================================================
# Implémentation de l'algorithme de Luhn sur les numéros AVS suisse
#
# Création d'un numéro AVS valide
#
# Vincent Keller, Gymnase de Beaulieu, (c) 2025
# ================================================================================

import random

numero = [7,5,6]

# Création des numéros 4 à 12 (au hasard)
i = 3
while i < 12:
    num = random.randint(0,9)
    numero.insert(i,num)
    i = i + 1

numero_original = numero.copy()

# Calcul du chiffre de contrôle (selon https://sozialversicherungen.admin.ch/fr/d/6938/download)
i = 11
while i >= 0:
    numero[i] = numero[i] * 3
    i = i - 1
somme = 0
i = 0
while i < len(numero):
    somme = somme + numero[i]
    i = i + 1

numero_original.append(10 - (somme%10))

print("Numéro AVS valide : ",numero_original)