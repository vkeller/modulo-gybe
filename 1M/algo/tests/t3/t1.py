taille = float(input("Entrez la taille"))
nops = 0
estim = 1
i = 1

for i in range(int(taille + 1)):
    if (i < taille + 1):
        estim = 1 + 1/estim
        i = i + 1
        nops = nops + 1
print(estim,nops)
        
