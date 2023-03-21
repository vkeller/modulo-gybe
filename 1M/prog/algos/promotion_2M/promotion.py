francais = 4
langue2 = 4
langue3 = 4
maths = 4
informatique = 4
chimie = 4
physique = 4
histoire = 4
ecodroit = 4
artsvisusmusique = 4
os = 4

notes = [francais,langue2,langue3,maths,informatique,chimie,physique,histoire,ecodroit,artsvisusmusique,os]

promu = False

# Règle 1 : obtenir un total des notes égal à au moins autant de fois 4 points qu'il y a de notes ;
regle1 = 0
for i in range(len(notes)):
    regle1 = regle1 + notes[i]

# Règle 2 : obtenir au moins 16 points dans un groupe constitué du français, de la moyenne des moyennes des notes de la deuxième langue nationale et de la troisième langue, arrondie au demi-point, des mathématiques et de l'option spécifique ;
regle2 = francais + (langue2 + langue3)/2 + maths + os

# Règle 3 : ne pas avoir plus de quatre notes inférieures à 4.
regle3 = 0
for i in range(len(notes)):
    if notes[i] < 4:
        regle3 = regle3 + 1

# Calcul de la promotion
if regle1 >= len(notes)*4:
    if regle2 >=16:
        if regle3 < 4:
            promu = True

if promu:
    print("Vous êtes promu.e en 2ème")
else:
    print("Vous n'êtes pas promu.e en 2ème")