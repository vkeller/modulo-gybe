# ------------------------------------------------------------------------
# Algorithme de tri des déchets
# - trier plusieurs déchets (boucle)
# - Demander le type d'objet (choix parmi : "plastique", "verre", "papier", "autre")
# - Selon le type :
#     - Si "plastique" → Afficher "Mettre dans la poubelle jaune"
#     - Si "verre" → Afficher "Mettre dans la poubelle verte"
#     - Si "papier" → Afficher "Mettre dans la poubelle bleue"
#     - Sinon → Afficher "Mettre dans la poubelle grise"
# Vincent Keller, Gymnase de Beaulieu, 2025
# ------------------------------------------------------------------------

print("Quel type de déchet souhaitez-vous jeter ?")
print("  1 : plastique : poubelle jaune")
print("  2 : verre     : poubelle verte")
print("  3 : papier    : poubelle bleue")
print("  4 : autre     : poubelle grise")

dechet = "-1"

while dechet != 0 :
    dechet = int(input("Quel type de déchet (0 lorsque tous les déchets sont triés) : "))
    if dechet == 1:
        print("Poubelle jaune")
    elif dechet == 2:
        print("Poubelle verte")
    elif dechet == 3:
        print("Poubelle bleue")
    else :
        if dechet != 0:
            print("Poubelle grise")

print("Merci pour votre responsabilité environnementale")
