longueur = 20
nops = 0
somme_des_carres = 0
for i in range(longueur):
    for j in range(longueur):
        somme = i + j
        somme_des_carres = somme_des_carres + somme
        nops = nops + 2
print(nops)
        