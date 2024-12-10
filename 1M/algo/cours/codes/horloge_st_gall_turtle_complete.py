# ------------------------------------------------------
# Simulation de l'horologe de la gare de St-Gall
#
# Prérequis :
# - fonctions
# - modules (time, datetime et turtle)
# - listes
# - boucles while
# - boucles for
# - tests
#
# (c) 2024, Vincent Keller, gymnase de Beaulieu, Lausanne
# ------------------------------------------------------

from datetime import datetime
from turtle import *
from time import *

# Fonction qui dessine un carré de taille et couleur précisée
def carre(t,s,taille,couleur):
    t.pensize(taille)
    t.pencolor(couleur)    
    s = s/1.3
    for i in range(4):
        t.forward(s)
        t.left(90)

# Fonction qui dessine un cercle de taille et couleur précisée
def rond(t,s, taille, couleur):
    t.pensize(taille)
    t.pencolor(couleur)
    s = s/2.5
    t.circle(s)

# Fonction qui dessine une croix de taille et couleur précisée
def croix(t,s,taille,couleur):
    t.pensize(taille)
    t.pencolor(couleur)    
    t.left(45)
    t.forward(s)
    t.left(180)
    t.forward(s/2)
    t.right(90)
    t.forward(s/2)
    t.left(180)
    t.forward(s)
    t.left(180)
    t.forward(s/2)
    t.left(90)
    t.forward(s/2)
    t.left(135)

# Fonction qui permet de tracer des ronds, des carrés et des croix
# à partir d'une liste de longueur quelconque mais déclarée
# avec des valeurs booléennes
def tracer(b,t,s,type):
    pos = t.pos()
    for i in range(len(b)-1,-1,-1):
        if b[i] == True:
            if type == "h":
                rond(t,s,6,"blue")
            elif type == "m":
                croix(t,s,6,"blue")
            else:
                carre(t,s,6,"blue")
            t.penup()
            t.back(s)
            t.pendown()
        else:
            if type == "h":
                rond(t,s,1,"blue")
            elif type == "m":
                croix(t,s,1,"blue")
            else:
                carre(t,s,1,"blue")
            t.penup()
            t.back(s)
            t.pendown()
    t.penup()
    t.goto(pos)
    t.pendown()
            
t = Turtle()

wn = Screen()
wn.tracer(0) 

# Boucle qui ne s'arrête jamais (dessine les éléments et dort 0.5 secondes
while True : 
    horloge = datetime.now()
    
    # Récupère l'heure actuelle
    heures = horloge.hour
    minutes = horloge.minute
    secondes = horloge.second

    # Construit les listes de booléens (conversion dec -> bin)
    p = 4
    h = [False, False, False, False, False]
    while p >= 0 :
        if heures - 2**p >= 0:
            heures = heures - 2**p
            h[4-p] = True
        p = p - 1

    p = 5
    m = [False, False, False, False, False, False]
    while p >= 0 :
        if minutes - 2**p >= 0:
            minutes = minutes - 2**p
            m[5-p] = True
        p = p - 1

    p = 5
    s = [False, False, False, False, False, False]
    while p >= 0 :
        if secondes - 2**p >= 0:
            secondes = secondes - 2**p
            s[5-p] = True
        p = p - 1

    size = 40

    # place les différents éléments sur la fenêtre
    # il y a un peu de déplacements pour pouvoir
    # placer les cercles, les carrés et les croix
    # au bon endroit (méthode try and fail)
    t.penup()
    t.forward(size/2.6)
    t.pendown()
    tracer(h,t,size,"h")
    t.penup()
    t.back(size/2.6)
    t.pendown()
    t.penup()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.pendown()
    tracer(m,t,size,"m")
    t.penup()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.pendown()
    tracer(s,t,size,"s")

    print(h)
    print(m)
    print(s)
    print("SBB -- CFF -- FFS")
    
    wn.update() 
    sleep(0.5)
    t.clear()
    t.penup()
    t.home()
    t.pendown()



