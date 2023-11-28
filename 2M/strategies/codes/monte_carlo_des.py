import random
import matplotlib.pyplot as plt

de1 = 0
de2 = 0
somme = 0
nb_exp = int(input("Nombre d'expériences : "))
reel = [(1/36)*100,(2/36)*100,(3/36)*100,(4/36)*100,(5/36)*100,(6/36)*100,(5/36)*100,(4/36)*100,(3/36)*100,(2/36)*100,(1/36)*100]

repart = []
values = []
diff = []

graph = False

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


repart.pop(0)
repart.pop(0)

for i in range(11):
    diff.append(repart[i]-reel[i])
    reel[i] = format(reel[i],'.2f')
    repart[i] = format(repart[i],'.2f')
    diff[i] = format(diff[i],'.2f')
    

print(repart)
print(reel)
print(diff)


if graph:
    plt.bar(values,repart)
    plt.xlabel('valeurs')
    plt.ylabel('nombres')
    plt.title('Distribution des sommes')
    plt.show()
