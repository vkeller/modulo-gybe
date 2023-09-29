# Racine d'Heron d'Alexandrie monitoré
# La racine à rechercher est fixée : 2.0
# Vincent Keller, 2023
import time
a = 2.0
limite = 20000000

for i in range(1000000,limite,100000):
    start = time.time()
    lim = i
    xn = a
    for i in range(lim):
        xnp1 = 0.5 * (xn + a/xn)
        xn = xnp1
    end = time.time()
    print(i,"\t",(end-start))