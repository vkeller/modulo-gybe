# Racine d'Heron d'Alexandrie
# Vincent Keller, 2023
a = float(input("Entrez la valeur de a : "))
lim = int(input("Entrez la limite      : "))
xn = a
for i in range(lim):
    xnp1 = 0.5 * (xn + a/xn)
    xn = xnp1
print("Racine de "+str(a)+" = "+str(xnp1))