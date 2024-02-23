nt = int(input("Nombre de termes : "))
estimation = 1
factoriel = 1

nops = 1

for i in range(1, nt):
    factoriel = factoriel * i
    estimation = estimation + 1/factoriel
    nops = nops + 3
    
print("Estimation : ", estimation, nops)