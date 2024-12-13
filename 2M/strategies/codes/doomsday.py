def bissextile(annee):
    ret = False
    if (annee%4 == 0) :
        if (annee%100 != 0) :
            if (annee%400 != 0) :
                ret = True
        else:
            ret = True
    return ret

def balise_siecle(annee):
    siecle = int((annee - annee%100)/100)%4
    bal = [2,0,5,3]
    return bal[siecle]

def jour_clef(annee,balise):
    annee_2 = annee%100
    if annee_2%2 != 0:
        annee_2 = int(annee_2 + 11)
    annee_2 = int(annee_2 / 2)
    if annee_2%2 != 0:
        annee_2 = int(annee_2 + 11)
    annee_2 = 7 - annee_2%7
    annee_2 = (annee_2 + balise)%7
    return annee_2

print("Quel jour êtes-vous né.e ? Entrez votre date de naissance")
jour = int(input("Jour   (jj)   : "))
mois = int(input("Mois   (mm)   : "))
annee = int(input("Année (aaaa) : "))

## Etape 1 : déterminer la balise du siècle

balise = balise_siecle(annee)

## Etape 2 : jour clef
jour_cle = jour_clef(annee,balise)

## Etape 3 : jour pivot

jc = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi', 'Samedi']
ordinaire = [10,28,14,4,9,6,11,8,5,10,7,12]
bisext    = [11,29,14,4,9,6,11,8,5,10,7,12]


mois = mois - 1
if bissextile(annee):
    j = (jour_cle + (jour-bisext[mois]+35)%7)%7
    print("le",jour,mois+1,annee,"est un ",jc[j])
else:
    j = (jour_cle + (jour-ordinaire[mois]+35)%7)%7
    print("le",jour,mois+1,annee,"est un ",jc[j])
    