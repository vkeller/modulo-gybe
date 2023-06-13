import tkinter as tk
import random as r
import time

def init_plat(plateau,h,l):
    for i in range(h):
        for j in range(l):
            plateau[i][j] = r.randint(0,1)

def init_plat2(plateau,h,l):
    cx = int(h/2)
    cy = int(l/2)
    plateau[cx][cy] = 1
    plateau[cx][cy+1] = 1
    plateau[cx][cy+2] = 1
    plateau[cx+1][cy] = 1
    plateau[cx+2][cy] = 1
    plateau[cx+2][cy+1] = 1
    plateau[cx+2][cy+2] = 1

def init_plat3(plateau,h,l):
    cx = int(h/2)
    cy = int(l/2)
    plateau[cx][cy] = 1
    plateau[cx+1][cy+1] = 1
    plateau[cx+1][cy-1] = 1
    plateau[cx+2][cy+1] = 1
    plateau[cx+2][cy-1] = 1
    plateau[cx+3][cy] = 1

def dessine(plateau):
    canv.delete('all')
    for x in range(hauteur):
        for y in range(largeur):
            if plateau[x][y] == 1:
                x1 = x*taille
                y1 = y*taille
                x2 = x1 + taille
                y2 = y1 + taille
                canv.create_rectangle(x1,y1,x2,y2,fill='black')

def calcule_cellule(plateau,x,y):
    ret = 0
    NW = plateau[x-1][y+1]
    N = plateau[x][y+1]
    NE = plateau[x+1][y+1]
    E = plateau[x+1][y]
    W = plateau[x-1][y]
    SW = plateau[x-1][y-1]
    S = plateau[x][y-1]
    SE = plateau[x+1][y-1]
    somme = NE+N+NW+E+W+SE+S+SW

    if plateau[x][y] == 1:
        if somme == 2 or somme == 3:
            ret = 1
        else:
            ret = 0
    if plateau[x][y] == 0:
        if somme == 3:
            ret = 1
        else:
            ret = 0
    return ret

def calcule_cellule_donut(plateau,x,y,h,l):
    ret = 0
    NW = plateau[(x-1+h)%h][(y+1+l)%l]
    N = plateau[(x+h)%h][(y+1+l)%l]
    NE = plateau[(x+1+h)%h][(y+1+l)%l]
    E = plateau[(x+1+h)%h][(y+l)%l]
    W = plateau[(x-1+h)%h][(y+l)%l]
    SW = plateau[(x-1+h)%h][(y-1+l)%l]
    S = plateau[(x+h)%h][(y-1+l)%l]
    SE = plateau[(x+1+h)%h][(y-1+l)%l]
    somme = NE+N+NW+E+W+SE+S+SW

    if plateau[x][y] == 1:
        if somme == 2 or somme == 3:
            ret = 1
        else:
            ret = 0
    if plateau[x][y] == 0:
        if somme == 3:
            ret = 1
        else:
            ret = 0
    return ret



taille = 10
hauteur = 100
largeur = 100

h = hauteur * taille
l = largeur * taille

jeu = []
jeu = [[0] * hauteur for i in range(largeur)]
jeu2 = []
jeu2 = [[0] * hauteur for i in range(largeur)]

init_plat3(jeu,hauteur,largeur)

racine = tk.Tk()
canv = tk.Canvas(racine, bg="white", height = h, width = l)
canv.pack()
steps = 10
for n in range(steps):
#    for i in range(1,hauteur-1):
#        for j in range(1,largeur-1):
#            jeu2[i][j] = calcule_cellule(jeu,i,j)

# Version donut
    dessine(jeu)
    canv.update()
    for i in range(hauteur):
        for j in range(largeur):
            jeu2[i][j] = calcule_cellule_donut(jeu,i,j,hauteur,largeur)
    time.sleep(1)
    print("step ",n)
    jeu = jeu2


racine.mainloop()