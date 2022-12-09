H = 1
M = 2
S = 3

Hb = [False, False, False, False, False]
Mb = [False, False, False, False, False, False]
Sb = [False, False, False, False, False, False]


# Traiter les heures
for i in range(4,-1,-1):
    if (pow(2,i) <= H):
        H = H - pow(2,i)
        Hb[len(Hb)-i-1] = True

# Traiter les minutes
for i in range(5,-1,-1):
    if (pow(2,i) <= M):
        M = M - pow(2,i)
        Mb[len(Mb)-i-1] = True

# Traiter les secondes
for i in range(5,-1,-1):
    if (pow(2,i) <= S):
        S = S - pow(2,i)
        Sb[len(Sb)-i-1] = True

print(Hb)
print(Mb)
print(Sb)
