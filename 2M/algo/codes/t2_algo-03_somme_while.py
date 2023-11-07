longueur = 5
nops = 0
sdp = 0
i = 0
while i < longueur:
    j = 0
    while j  < longueur:
        somme = i + j
        sdp = sdp + somme
        j = j + 1
        nops = nops + 3
    i = i + 1
    nops = nops + 2
print(sdp,nops)