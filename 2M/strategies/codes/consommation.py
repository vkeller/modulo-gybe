nbrpersonnes = int(input("Combien de personnes dans le ménage : "))
consototalejour = 0
i = 0
while i < nbrpersonnes:
    phrase = "Quel est le profile de la personne "+str(i)+" (E/S/G)"
    profile = input(phrase)
    if profile == "E":
        consototalejour = consototalejour + 112
    elif profile == "S":
        consototalejour = consototalejour + 140
    else :
        consototalejour = consototalejour + 168
    i = i + 1
consomensuelle = consototalejour * 30
moyenneparpersonne = consototalejour/nbrpersonnes
if moyenneparpersonne < 120:
    print(moyenneparpersonne, "litres. Ecoresponsable !")
else:
    print(moyenneparpersonne, "litres. Consommation élevée !")
print("Consommation mensuelle :", consomensuelle, "litres")