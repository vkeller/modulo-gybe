nt = int(input("Nombre d'itérations : "))
nops = 0
x = 2
i = 1
while i < nt:
    x = 0.5 * (x + 2/x)
    i = i + 1
    nops = nops + 1
print(x,nops)
