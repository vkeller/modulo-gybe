# Jeu du pendu v5 : Demande d'un mot à l'utilisateur, finalisation des messages du jeu 
# (c) Vincent Keller, 2023
nbrEssais = 3
nbrLettresTrouvees = 0
motATrouver = input("Entrez un mot à trouver : ")
print(list(motATrouver))
motTrouve = []
for i in range(len(motATrouver)):
    motTrouve.append("-")
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
        print("Bravo ! Vous avez trouvé le mot ")
        j = nbrEssais

if nbrLettresTrouvees != len(motATrouver):
    print("Dommage... recommencez")
