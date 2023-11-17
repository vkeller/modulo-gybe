carte_invalide = [5,6,3,5,4,0,0,2,9,5,6,1,3,4,1,1]
carte_valide = [4,9,5,0,4,8,4,7,7,7,5,2,5,9,5,5]
carte_valide2 = [5,1,3,6,5,9,0,4,3,0,3,6,8,7,4,2]
carte = carte_valide2
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
else:
    print("carte invalide")
