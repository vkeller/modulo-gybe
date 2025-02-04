import random
atrouver = random.randint(1,100)

x = -1

while x != atrouver:
    x = int(input("Entrez un chiffre : "))
    if x < atrouver :
        print("trop petit")
    elif x > atrouver :
        print("trop grand")
    else:
        print("Bravo")