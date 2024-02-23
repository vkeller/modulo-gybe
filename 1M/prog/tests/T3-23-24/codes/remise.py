montant = float(input("Entrez le montant de l'achat en CHF : "))
type_client = input("Entrez le type de client (normal/premium) : ").lower()

remise = 0

if montant > 50:
    remise = montant * 0.05  # Calcul de la remise de base
    if type_client == "premium":
        remise += montant * 0.10  # Remise supplémentaire pour les clients premium

montant_final = montant - remise
print(f"Le montant final après remise est de {montant_final} CHF.")

