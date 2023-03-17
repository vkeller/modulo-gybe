## Algorithmes simples

def algo1():
    n = 3987.4
    for i in range(30):
        m = (n + 1/n)/2
        print (m)
        n = m

def algo2():
    n = 3987.4
    for i in range(50):
        m = 1 + 1/n
        print(m)
        n = m

def algo3():
    n = 30
    for i in range(50):
        m = 1/4*n + 2
        print(m)
        n = m

def algo4():
    n = 30
    for i in range(50):
        m = 1/2*n + 1
        print(m)
        n = m

algo4()