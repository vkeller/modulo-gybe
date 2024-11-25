import random

trouve = False

a = random.randint(1,40)
b = random.randint(1,a)

print("Bonjour Magda, c'est GoMath")
print("Combien font",a,"-",b,"?")

while trouve == False :
    entree = int(input("Donne-moi le résultat : "))
    if entree == (a-b):
        print("BRAVO !!")
        trouve = True
    else:
        print("Faux ! Recommence !")

