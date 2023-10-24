def sommeEntiers(n):
    somme = 0
    for i in range(n+1):
        somme += i
    return somme
for i in range(1000):
    p = sommeEntiers(i)
    print(i,"\t",p)
