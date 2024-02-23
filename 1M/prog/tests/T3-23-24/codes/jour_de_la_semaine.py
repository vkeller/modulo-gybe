# Remarque : // signifie "Division entière" : on ne garde que la partie
# entière. Exemple : 5//2 = 2
jour = int(input("Quel jour sommes-nous (1-31) : "))
mois = int(input("Quel mois sommes-nous (1-12) : "))
annee = int(input("Quelle année sommes-nous : "))

jourDeLaSemaine = ""

c = (14-mois)//12
a = annee - c
m = mois + 12 * c - 2

j = (jour + a + a//4 - a//100 + a//400 + (31*m)//12 ) % 7

if annee < 1583 or annee > 9999 :
    print("L'algorithme ne fonctionne pas pour l'année",annee)
else:
    if j == 1 :
        jourDeLaSemaine = "lundi"
    elif j == 2 :
        jourDeLaSemaine = "mardi"
    elif j == 3 :
        jourDeLaSemaine = "mercredi"
    elif j == 4 :
        jourDeLaSemaine = "jeudi"
    elif j == 5 :
        jourDeLaSemaine = "vendredi"
    elif j == 6 :
        jourDeLaSemaine = "samedi"
    elif j == 0 :
        jourDeLaSemaine = "dimanche"
    print("Nous sommes",jourDeLaSemaine)
