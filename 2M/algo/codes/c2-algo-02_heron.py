n = int(input("Entrez la racine à calculer : "))
limite = int(input("Entrez la limite : "))
xn = n
i = 0
for i in range(limite):
    xnp1 = 0.5 * (xn + n/xn)
    xn = xnp1
print("Racine de ",n," : ",xnp1)