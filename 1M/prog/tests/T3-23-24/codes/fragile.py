poids = float(input("Entrez le poids de la marchandise en Kg : "))
fragile = input("La marchandise est-elle fragile ? (oui/non) : ").lower()

if fragile == "oui":
    fragile = True
else:
    fragile = False

cout_total = 0
    
if poids > 5:
    cout_total = (poids - 5)  # Coût pour chaque kilo supplémentaire au-delà de 5 Kg
if fragile:
    cout_total += 5  # Surtaxe pour la marchandise fragile

print(f"Le coût d'expédition est de {cout_total} CHF.")

