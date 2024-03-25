nt = int(input("Entrez nt : "))
signe = 1
nops = 0
estim = 0
for i in range(1,nt*2,2):
    estim = estim + (signe * (4/i))
    nops = nops + 1
print(estim, nops)