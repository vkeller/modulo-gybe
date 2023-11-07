longueur = 2
nops = 0
sds = 0
i = 0
while i < longueur:
    j = 0
    while j  < longueur:
        k = 0
        while k  < longueur:
            p = i + j + k
            sds = sds + p
            k = k + 1
            nops = nops + 3
        j = j + 1
        nops = nops + 2
    i = i + 1
    nops = nops + 2
print(sds,nops)
