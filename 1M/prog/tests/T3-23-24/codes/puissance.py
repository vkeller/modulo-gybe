base = int(input("Entrez la base : "))
exposant = int(input("Entrez l'exposant : "))
resultat = 1

if exposant < 0:
    for i in range(-exposant):
        resultat = resultat / base
else:
    for i in range(exposant):
        resultat = resultat * base

print(base, "élevé à la puissance", exposant, "est égal à", resultat)
