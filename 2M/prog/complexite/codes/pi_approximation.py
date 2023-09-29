# Approximation du nombre Pi
# avec la formule de Leibnitz
# sum_{k = 0}^{\infty} = \frac{-1^k}{2k + 1}
# Vincent Keller, 2023
import math
pi = 0
limite = 10000000
for i in range(0,limite,1):
    pi = pi + (pow(-1,i))/(2*i + 1)
pi = pi * 4
print(pi)