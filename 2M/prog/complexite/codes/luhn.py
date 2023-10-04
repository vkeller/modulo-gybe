# Algorithme de Luhn - wagons de chemin de fer
# Vincent Keller, 2023

identification = []
for i in range(11):
    identification.append(int(input("Entrez le chiffre "+str(i+1)+" : " )))
print(identification)
somme = 0
for i in range(11):
    tmp = 0
    if i%2 == 0 :
        tmp = identification[i]*2
    else:
        tmp = identification[i]
    if (tmp - 10 >=0):
        somme = somme + tmp%10 + 1
    else:
        somme = somme + tmp
if somme%10 != 0:
    controle = 10 - somme%10
else:
    controle = 0
immatriculation = ""
immatriculation += str(identification[0])
immatriculation += str(identification[1]) + "-"
immatriculation += str(identification[2])
immatriculation += str(identification[3]) + "-"
immatriculation += str(identification[4])
immatriculation += str(identification[5])
immatriculation += str(identification[6]) + " "
immatriculation += str(identification[7]) + " "
immatriculation += str(identification[8])
immatriculation += str(identification[9])
immatriculation += str(identification[10]) + " "
immatriculation += str(controle)
print("Immatriculation du wagon : "+immatriculation)
# 21-81-247 1 217
# 3 1 - 8 1 - 6 6  5 0 2 8  6
#  5 1 - 8 0 - 0 8 4 3 0 0 1