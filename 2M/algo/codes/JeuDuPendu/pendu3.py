# Jeu du pendu v3 : affichage intermédiaire
# (c) Vincent Keller, 2023
motATrouver = ['P','E','N','D','U']
motTrouve = ['-','-','-','-','-']
nbrEssais = 9
j = 0
while (j < nbrEssais) :
    lettre = input("Entrez une lettre : ")
    for i in range(len(motATrouver)):
        if motATrouver[i] == lettre :
            #print("La lettre "+lettre+" se trouve dans le mot")
            motTrouve[i] = lettre
    j = j + 1
    print(motTrouve)

