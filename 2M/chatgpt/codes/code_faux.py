from turtle importe *

def triangle(cote,t) :
    i = 0
    while i < 3 :
        t.forward(cote)
        t.left(120)

tortue = turtle()

couleur = "verts"

if couleur =! "red":
    print("Ce n'est pas la bonne coleur")
else:
    tortue.Pencolor(couleur)

triangle(100,tortue)
