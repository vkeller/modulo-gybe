import turtle

stylo = turtle.Turtle()
stylo.speed(5)

# === Triangle du bas (150 de côté) ===
stylo.penup()
stylo.goto(-75, -50)
stylo.pendown()
stylo.color("darkgreen")
stylo.pensize(3)

cote = 0
while cote < 3:
    stylo.forward(150)
    stylo.left(120)
    cote += 1

# === Triangle du milieu (120 de côté) ===
stylo.penup()
stylo.goto(-60, 20)
stylo.pendown()
stylo.color("green")
stylo.pensize(3)

cote = 0
while cote < 3:
    stylo.forward(120)
    stylo.left(120)
    cote += 1

# === Triangle du haut (90 de côté) ===
stylo.penup()
stylo.goto(-45, 80)
stylo.pendown()
stylo.color("lightgreen")
stylo.pensize(3)

cote = 0
while cote < 3:
    stylo.forward(90)
    stylo.left(120)
    cote += 1

# === Tronc : rectangle VERTICAL, centré ===
# On part du coin inférieur GAUCHE du tronc
stylo.penup()
stylo.goto(-15, -100)   # bas du tronc, centré sous les triangles
stylo.setheading(0)     # assure orientation vers la droite
stylo.pendown()
stylo.color("saddlebrown")
stylo.pensize(5)

# Tracer le rectangle avec une boucle while (4 côtés)
cote = 0
largeur = 30
hauteur = 50
while cote < 4:
    if cote == 0:
        stylo.forward(largeur)   # base (vers la droite)
        stylo.left(90)
    elif cote == 1:
        stylo.forward(hauteur)   # côté gauche (vers le haut)
        stylo.left(90)
    elif cote == 2:
        stylo.forward(largeur)   # sommet (vers la gauche)
        stylo.left(90)
    else:  # cote == 3
        stylo.forward(hauteur)   # côté droit (vers le bas)
        # pas besoin de tourner après
    cote += 1

stylo.hideturtle()
turtle.done()