nt = int(input("Combien de termes : "))
estimation = 0
signe = 1

nops = 0

for i in range(1,nt*2,2):
    estimation = estimation + signe * (4/i)
    signe = signe * -1
    nops = nops + 4

print("Estimation",estimation, nops)