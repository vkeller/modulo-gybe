# ---------------------------------------------------
# Passerelle 3C->2M
# Correction exercice 3
#
# Vincent Keller, Gymnase de Beaulieu, Lausanne, 2025
# ---------------------------------------------------

nombre = 10
trouve = False
while trouve != True:
    tentative = int(input("Entrez un nombre : "))
    if tentative == nombre:
        print("Bravo ! Vous avez trouvé",nombre)
        trouve = True
    else:
        print("Non... recommencez !")
