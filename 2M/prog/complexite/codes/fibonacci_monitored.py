# Suite de Fibonacci monitoré
# Vincent Keller, 2023
import time


# Nombre d'opérations ou d'instructions
N = 0

for t in range(100,100000,100):
    borneSup = t
    fib = []
    fib.append(0)
    fib.append(1)
    N = N + 3

    for i in range(2,borneSup,1):
        fib.append(0)
        N = N + 1

    start = time.time()
    for i in range(2,borneSup,1):
        fib[i] = fib[i-1] + fib[i-2]
        N = N + 1
    end = time.time()

    fib.clear()

    print(t,"\t",end-start)

    N = 0
