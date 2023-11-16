x = int(input("Entrez un chiffre positif : "))

if x < 0:
    raise Exception("Désolé, le nombre doit être supérieur à zéro")
else:
    print("Vous avez entré : ",x)
print("Fin du programme")