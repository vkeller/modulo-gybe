produits = ["Lait", "Pain", "Viande", "Fruits", "Fromage", "Eau"]
prix = [2, 1.5, 25, 8, 22, 3]
prix_final = []

for i in range(len(produits)):
    if prix[i] > 20:
        prix_final.append(prix[i] * 0.9)  # Réduction de 10%
    elif prix[i] < 5:
        prix_final.append("Promo")
    else:
        prix_final.append(prix[i])

for i in range(len(produits)):
    if prix_final[i] == "Promo" :
        print(produits[i], "est en promotion")
    else:
        print(produits[i], "est au prix de ", prix_final[i], "CHF")
        