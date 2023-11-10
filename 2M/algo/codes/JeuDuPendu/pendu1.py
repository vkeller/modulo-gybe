# Jeu du pendu v1 : test d'une lettre
# (c) Vincent Keller, 2023
motATrouver = ['P','E','N','D','U']
lettre = input("Entrez une lettre : ")
for i in range(len(motATrouver)):
    if motATrouver[i] == lettre :
        print("La lettre "+lettre+" se trouve dans le mot")