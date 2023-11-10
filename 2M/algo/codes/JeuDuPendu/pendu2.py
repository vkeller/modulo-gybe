# Jeu du pendu v2 : test de plusieurs lettres
# (c) Vincent Keller, 2023
motATrouver = ['P','E','N','D','U']
nombreEssais = 9
j = 0
while (j < nbrEssais) :
    lettre = input("Entrez une lettre : ")
    for i in range(len(motATrouver)):
        if motATrouver[i] == lettre :
            print("La lettre "+lettre+" se trouve dans le mot")
    j = j + 1