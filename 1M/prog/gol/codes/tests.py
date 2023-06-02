import tkinter as tk
import random as r

taille = 3
hauteur = 300
largeur = 300

h = hauteur * taille
l = largeur * taille

jeu = []
jeu = [[0] * hauteur for i in range(largeur)]
nbr = 0;
for i in range(hauteur):
    for j in range(largeur):
        jeu[i][j] = r.randint(0,1)
        if jeu[i][j] == 1:
            nbr += 1
racine = tk.Tk()
canv = tk.Canvas(racine, bg="white", height = h, width = l)
canv.pack()

for x in range(hauteur):
    for y in range(largeur):
        if jeu[x][y] == 1:
            canv.create_rectangle(x*taille,y*taille,(x*taille)+taille,(y*taille)+taille,fill='black')

    
racine.mainloop()