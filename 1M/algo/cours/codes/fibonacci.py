# ================================================================================
# Implémentation de la suite de Fibonacci non récursive
#
# Entrée de l'algorithme : n qui correpond aux n premiers nombres de Fibonacci
#
# Vincent Keller, Gymnase de Beaulieu, (c) 2025
# ================================================================================
a = 1
b = 1
n = int(input("Combien de nombres de Fibonacci voulez-vous ? "))
i = 0
print(a)
print(b)
while i < n-2:
    a = a + b
    b = a - b
    print(a)
    i = i + 1