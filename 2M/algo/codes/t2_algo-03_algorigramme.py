taille = 1
nops = 0
phi = 1.
for i in range(1,taille+1,1):
    phi = 1 + 1/phi
    nops = nops + 1
print(phi,nops)