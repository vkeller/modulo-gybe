def pasDaccord():
    print("On n'accorde pas")
def accordCVD():
    print("On accorde avec le CVD")

# Fonction qui demande à l'utilisateur de répondre par
# la chaîne de caractères "oui" ou la chaîne de caractères "non"
# Entrée quest (type string) : la question à poser
# Sortie ret (type bool) : True (oui) ou False (non)
def question(quest):
    q = input(quest+" (oui/non) ?")
    if q == "oui":
        ret = True
    else:
        ret = False
    return ret
    
pronominal = question("Le verbe est-il un verbe pronominal")
oui = True
non = False
if pronominal == True :
    unAutre = question("Est-ce que le 'se' signifie 'l'un l'autre'")
    if unAutre == True:
        pasDaccord()
    else:
        CVD1 = question("Y a-t-il un CVD ? ")
        if CVD1 == True:
            print("Utiliser la règle d'accord de l'auxiliaire avoir")
        else:
            print("Utiliser la règle d'accord de l'auxiliaire être ")
else:
    auxiliaire = question("Est-ce que c'est l'auxiliaire avoir")
    if auxiliaire == True:
        pp = input("Le participe est-il suivi d'un infinitif")
        if pp == True:
            laisserFaire = question("Le participe est-il 'laissé' ou 'faire'")
            if laisserFaire == True:
                pasDaccord()
            else:
                CVD2 = question("Le CVD est-il placé avant le sujet ET en lien avec l'infinitif")
                if CVD2 == True:
                    accordCVD()
                else:
                    pasDaccord()
        else:
            CVD3 = question("Le CVD est-il placé avant le sujet")
            if CVD3 == True: 
                accordCVD()
            else:
                pasDaccord()
    else:
        print("On accorde avec le sujet")