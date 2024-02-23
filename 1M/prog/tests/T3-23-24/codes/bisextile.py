annee_debut = int(input("Entrez l'année de début : "))
annee_fin = int(input("Entrez l'année de fin : "))

print("Les années bissextiles entre", annee_debut, "et", annee_fin, "sont :")
for annee in range(annee_debut, annee_fin + 1):
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print(annee, "est une année bisextile ")
    else:
        print(annee,"n'est pas une année bisextile")


