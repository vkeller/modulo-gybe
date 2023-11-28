import random
import matplotlib.pyplot as plt

de1 = 0
de2 = 0
somme = 0
nb_exp = int(input("Nombre d'expériences : "))
repart = []
values = []

for i in range(13):
    repart.append(0)
    values.append(i)
for i in range(nb_exp):
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    somme = de1 + de2
    repart[somme] = repart[somme]+1
    
for i in range(13):
    repart[i] = repart[i]/nb_exp*100

print(repart)

plt.bar(values,repart)
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Distribution des sommes')
plt.show()