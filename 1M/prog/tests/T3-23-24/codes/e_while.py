nt = int(input("Nombre de termes : "))
estimation = 1
factoriel = 1

nops = 1

i = 1

while i < nt:
    factoriel = factoriel * i
    estimation = estimation + 1/factoriel
    nops = nops + 3
    i = i + 1
    
print("Estimation : ", estimation, nops)
