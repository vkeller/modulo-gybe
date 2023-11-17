import random
carte = []
carte.append(3)
for i in range(15):
    carte.append(random.randint(0,9))
limite = len(carte)
somme = 0
for i in range(0,limite,2):
    e = carte[i]*2
    if e>9 :
        e = e-9
    somme += e
for i in range(1,limite,2):
    somme += carte[i]
print(carte)
if (somme%10 == 0):
    print("carte valide")
    valide = True
else:
    print("carte invalide")


