nt = int(input("Nombre d'itérations : "))
nops = 0
x = 5
i = 1
while i < nt:
    x = 0.5 * (x + 5/x)
    i = i + 1
    nops = nops + 1
print(x,nops)