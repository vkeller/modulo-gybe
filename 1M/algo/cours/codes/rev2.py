original = [1, 2, 2, 3, 1, 4]
unique = []
i = 0

# Boucle 1 : Parcourir la liste originale
while i < len(original):
    element = original[i]
    exists = False
    j = 0
    
    # Boucle 2 : Vérifier si l'élément est déjà dans la liste unique
    while j < len(unique):
        # Test 1 : Vérifier l'égalité
        if unique[j] == element:
            exists = True
            break
        j += 1
    
    # Test 2 : Ajouter seulement si l'élément n'existe pas
    if not exists:
        unique.append(element)
    
    i += 1

print(f"Liste sans doublons : {unique}")