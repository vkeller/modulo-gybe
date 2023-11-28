import random

nb_exp = int(input("Nombre d'expériences : "))

values = []

for i in range(6):
    values.append(i)

for i in range(nb_exp):
    de1 = random.randint(1,6)
    values[de1-1] = values[de1-1]+1

for i in range(6):
    values[i] = values[i]/nb_exp
    
print(values)