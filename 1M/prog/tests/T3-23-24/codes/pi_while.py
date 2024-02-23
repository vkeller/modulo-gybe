nt = int(input("Combien de termes : "))
estimation = 0
signe = 1
i = 1

nops = 0

while nt > 0:
    estimation = estimation + signe * (4/i)
    signe = signe * -1
    i = i + 2
    nt = nt - 1 
    nops = nops + 6

print("Estimation",estimation, nops)
