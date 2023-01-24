age = int(input("Entrez votre âge"))

if (age< 18):
    print("Vous etes mineur")
    if (age >= 14):
        print("Vous êtes un ado")
    else:
        print("Vous êtes un enfant")        
else:
    if (age > 100):
        print("Vous êtes mort")
    else:        
        print("Vous etes majeur")
        if (age <= 65):
            print("Vous êtes actif")
        else:
            print("Vous êtes retraité")

