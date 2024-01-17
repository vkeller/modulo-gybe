taille = int(input("Taille "))
nops = 0
phi = 1
for i in range(taille):
    phi = 1 + 1/phi
    nops = nops + 1
    print(phi, nops)