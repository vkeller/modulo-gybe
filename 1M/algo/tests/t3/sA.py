taille = int(input("Entrez la taille : "))
nops = 0
estim = 1
i = 1
for i in range(taille + 1):
    estim = 1 + 1/estim
    nops = nops + 1
print(nops, estim)