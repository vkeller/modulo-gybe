# ---------------------------------------------------
# Passerelle 3C->2M
# Correction exercice 2
#
# Vincent Keller, Gymnase de Beaulieu, Lausanne, 2025
# ---------------------------------------------------

prenom = input("Quel est votre prénom : ")
age = input("Quel est votre âge : ")
genre = input("Quel est votre genre (f/m) : ")
age = int(age)
annee = 2025 - age
ne = "né"
if genre == "f":
    ne = ne+"e"
elif genre == "m" :
    ne = ne
else:
    ne = ne+".e.x"
print("Bonjour",prenom,"vous êtes",ne,"en",annee)
