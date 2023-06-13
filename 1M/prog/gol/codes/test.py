import turtle

# Créer une fenêtre graphique
window = turtle.Screen()

# Créer un objet Turtle
pen = turtle.Turtle()

# Dessiner le carré
for _ in range(4):
    pen.forward(100)  # Avancer de 100 pixels
    pen.right(90)     # Tourner de 90 degrés à droite

# Fermer la fenêtre lorsqu'on clique dessus
window.exitonclick()