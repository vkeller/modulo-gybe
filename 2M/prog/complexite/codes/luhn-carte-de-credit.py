# Algorithme de Luhn - Cartes de crédit
# Vincent Keller, 2023

numero = []
for i in range(15):
    if i == 0:
        numero.append(int(input("Entrez le "+str(i+1)+"er chiffre : " )))
    else:    
        numero.append(int(input("Entrez le "+str(i+1)+"ème chiffre : " )))

numero.append(int(input("Entrez la clef de contrôle : " )))
somme = 0
for i in range(16):
    tmp = 0
    if i%2 == 0 :
        tmp = numero[i]*2
    else:
        tmp = numero[i]
    if (tmp - 10 >=0):
        somme = somme + tmp%10 + 1
    else:
        somme = somme + tmp
#somme = somme + numero[15]
if somme%10 != 0:
    print("Numéro de carte invalide")
else:
    print("Numéro de carte valide")
# 5635 4002 9561 3411 (Invalide)
# 4396-8374-1204-2755 (Valide)
# 4624 7482 3324 9080 (Invalide)