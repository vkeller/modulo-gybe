# Jeu du pendu v4 : Ajout règle : si lettre trouvée alors nbrEssais = nbrEssais-1
# Et si mot trouvé alors sortie
# (c) Vincent Keller, 2023
motATrouver = ['P','E','N','D','U']
motTrouve = ['-','-','-','-','-']
nbrEssais = 3
nbrLettresTrouvees = 0
j = 0
while (j < nbrEssais) :
    lettre = input("Entrez une lettre : ")
    for i in range(len(motATrouver)):
        if motATrouver[i] == lettre :
            #print("La lettre "+lettre+" se trouve dans le mot")
            motTrouve[i] = lettre
            nbrLettresTrouvees = nbrLettresTrouvees + 1
            j = j - 1
    j = j + 1
    print(motTrouve)
    if nbrLettresTrouvees == len(motATrouver):
        j = nbrEssais
