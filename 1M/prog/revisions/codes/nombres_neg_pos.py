nombres = [10, -5, 3, -1, 20, -8, 7, 0, -12, 15]
positifs = []
negatifs = []
neutres = []

for i in range(len(nombres)):
    nombre = nombres[i]
    if nombre > 0:
        positifs.append(nombre)
    elif nombre < 0 :
        negatifs.append(nombre)
    else :
        neutres.append(nombre)

print("Il y a", len(negatifs),"nombres négatifs")
print("Il y a", len(neutres),"zéros")
print("Il y a", len(positifs),"nombres positifs")