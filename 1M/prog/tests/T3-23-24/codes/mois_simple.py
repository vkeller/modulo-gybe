mois = int(input("Entrez un mois (sous forme de nombre) : "))
annee = int(input("Entrez une année : "))

if mois == 2:
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print("Février", annee, "a 29 jours.")
    else:
        print("Février", annee, "a 28 jours.")
elif mois  == 4 or mois == 6 or mois == 9 or mois == 11:
    print("Le mois", mois, "a 30 jours.")
else:
    print("Le mois", mois, "a 31 jours.")