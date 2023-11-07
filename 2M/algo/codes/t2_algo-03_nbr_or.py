import math
import numpy as np
taille = 11
fibnp1 = np.longdouble(1)
fibnp2 = np.longdouble(2)
phi = np.longdouble(( 1 + math.sqrt(5) ) / 2)
for i in range(taille):
    tmp = fibnp1
    fibnp1 = fibnp1 + fibnp2
    fibnp2 = tmp
    print("Nombre d'or à ",i," = ",(fibnp1/fibnp2), " Epsilon : ",abs((fibnp1/fibnp2)-phi))
print("fibnp2 = ",fibnp2)
print("fibnp1 = ",fibnp1)
