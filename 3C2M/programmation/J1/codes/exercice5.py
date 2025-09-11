# ---------------------------------------------------
# Passerelle 3C->2M
# Correction exercice 5
#
# Vincent Keller, Gymnase de Beaulieu, Lausanne, 2025
# ---------------------------------------------------

# Fonction qui affiche la phrase "Bonjour prénom, vous êtes né en année"
def afficher(prenom, annee) :
    print("Bonjour",prenom,"vous êtes né en",annee)    

# Fonction qui calcule l'année de naissance en fonction de l'âge
# retourne l'année de naissance depuis l'année 2025
def calculeAnnee(age):
    annee = 2025 - age
    return annee

prenom = input("Quel est votre prénom : ")
age = input("Quel est votre âge : ")
age = int(age)
afficher(prenom,calculeAnnee(age))
