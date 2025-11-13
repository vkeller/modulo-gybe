taille = int(input("Quelle taille de carré : "))

for i in range(taille):
    ligne = ""
    for j in range(taille):
        if (j+i)%2 == 0:
            ligne = ligne+"X"
        else:
            ligne = ligne+"O"
    print(ligne)
    
