longueur = 5
nops = 0
sdp = 0
for i in range(longueur):
    for j in range(longueur):
        somme = i + j
        sdp = sdp + somme
        nops = nops + 2
print(sdp,nops)
        