for n in range(0,1000000,10000):
    s = 0
    nops = 0
    for i in range(n):
        a = i
        nops = nops + 1
        while a > 1:
            a = a/2
            nops = nops + 1
        s = s + 1
    print(n,"\t",nops)
