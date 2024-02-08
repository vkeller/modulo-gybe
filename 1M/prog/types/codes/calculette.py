# ==============================================
# Calculette capable de +, -, * et /
# 
# (c) 2024, Vincent Keller, gymnase de Beaulieu
# ==============================================
n1 = float(input("Premier nombre : "))
n2 = float(input("Second nombre  : "))
oper = input("Quelle opération voulez-vous (+,-,*,/) : ")
res = 0
if oper == "+":
    res = n1 + n2
elif oper == "-":
    res = n1 - n2
elif oper == "*":
    res = n1 * n2
elif oper == "/":
    if n2 == 0:
        print("Division par zéro !")
    else:
        res = n1 / n2
else:
    print(oper+" n'est pas une opération autorisée")
print("Résultat : ",res)