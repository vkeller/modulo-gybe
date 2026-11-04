from turtle import *

pencolor("darkgreen")
pensize(2)

taille = 10
compteur_marches = 0
max_marches = 15

# Boucle while contrôlée par un nombre maximal de marches
while compteur_marches < max_marches:
    # Monter la marche
    forward(taille)
    left(90)
    
    # Avancer sur le palier
    forward(taille)
    right(90)
    
    # La marche grandit pour la prochaine itération
    taille = taille + 12
    
    # Incrémentation du compteur pour éviter la boucle infinie
    compteur_marches = compteur_marches + 1

done()