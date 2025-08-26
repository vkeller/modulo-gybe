# -------------------------------------------------------
# Proposition de correction du TP supplémentaire
# R2-PROG-02 : Rappels 1M - mini-projet
# Vincent Keller, Gymnase de Beaulieu, 2025, licence BSD
# -------------------------------------------------------

budget = float(input("Quel est votre budget hebdomadaire (en CHF) : "))
depenses = []
categories = []
nom_cat = ["snack", "transports", "jeux", "autres"]


print("=== Suivi de budget hebdomadaire ===")
print("Saisis tes dépenses. Pour chaque dépense, précise le type.")
print("Types : 1=snack, 2=transport, 3=jeux, 4=autre")
print("Entre 0 comme montant pour terminer.")

montant = 1.0

while montant != 0 :
    montant = float(input("Montant de la dépense en CHF (0 pour finir) : "))
    
    if montant == 0.0:
        break
    
    depenses.append(montant)
    
    cat = int(input("Catégorie (0=snack, 1=transport, 2=jeux, 3=autre)"))
    
    categories.append(cat)
    
    total_temporaire = 0
    
    for i in range(len(depenses)):
        total_temporaire = total_temporaire + depenses[i]
    
    if total_temporaire > budget:
        print("Attention ! Budget hebdomadaire dépassé")
    else:
        print("Dépense enregistrée. Il reste",(budget-total_temporaire))

if len(depenses) == 0:
    print("Aucune dépense enregistrée.")
else:
    total = 0
    for i in range(len(depenses)):
        total = total + depenses[i]

    # Calcul de la moyenne
    moyenne = total / len(depenses)

    # Trouver la dépense la plus élevée (sans max)
    max_depense = depenses[0]
    for d in depenses:
        if d > max_depense:
            max_depense = d

    # Compter par catégorie
    nb_snack = 0
    nb_transport = 0
    nb_jeux = 0
    nb_autre = 0
    for c in categories:
        if c == 1:
            nb_snack += 1
        elif c == 2:
            nb_transport += 1
        elif c == 3:
            nb_jeux += 1
        elif c == 4:
            nb_autre += 1

    # Identifier la catégorie de la dépense maximale
    # On cherche l'indice de la première occurrence de max_depense
    index_max = 0
    for i in range(len(depenses)):
        if depenses[i] == max_depense:
            index_max = i
            break
    categorie_max = categories[index_max]
    nom_max = noms_categories[categorie_max]

    # Affichage final
    print("\n" + "="*40)
    print("       BILAN FINAL")
    print("="*40)
    print(f"Budget hebdomadaire : {budget:.2f} €")
    print(f"Nombre de dépenses : {len(depenses)}")
    print(f"Total des dépenses : {total:.2f} €")
    print(f"Moyenne par dépense : {moyenne:.2f} €")
    print(f"Dépense la plus élevée : {max_depense:.2f} € ({nom_max})")

    if total <= budget:
        print(f"✅ Bien joué ! Il te reste {budget - total:.2f} €.")
    else:
        print(f"❌ Budget dépassé de {total - budget:.2f} €.")

    print("\n--- Répartition par catégorie ---")
    print(f"Snacks : {nb_snack}")
    print(f"Transports : {nb_transport}")
    print(f"Jeux : {nb_jeux}")
    print(f"Autres : {nb_autre}")

    print("\n--- Détail des dépenses ---")
    for i in range(len(depenses)):
        montant = depenses[i]
        cat_num = categories[i]
        nom_cat = noms_categories[cat_num]
        print(f"  {montant:.2f} € → {nom_cat}")

p