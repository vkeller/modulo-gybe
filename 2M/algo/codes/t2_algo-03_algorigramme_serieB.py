taille = 1000
nops = 0
r2 = 1.
for i in range(1,taille+1,1):
    r2 = 1/(2. + r2)
    nops = nops + 1
print(r2,nops)
