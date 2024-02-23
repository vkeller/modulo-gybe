nombre = int(input("Entrez un nombre entier positif : "))

position = 1
print("Chiffres aux positions paires dans le nombre", nombre, ":")
while nombre > 0:
    chiffre = nombre % 10
    if position % 2 == 0:
        print(chiffre, end=" ")
    nombre //= 10
    position += 1
