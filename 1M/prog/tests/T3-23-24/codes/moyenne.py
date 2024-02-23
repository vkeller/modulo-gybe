n = int(input("Entrez le nombre de nombres : "))
somme = 0
i = 0
while i < n:
    nombre = float(input("Entrez un nombre : "))
    somme += nombre
    i += 1
moyenne = somme / n
print("La moyenne des nombres saisis est", moyenne)
if moyenne < 4.0:
    print("Vous avez raté cette branche")
else:
    print("Vous avez réussi cette branche")
