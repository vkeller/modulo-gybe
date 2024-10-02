limite = 1000000
tableau = []
for i in range(limite):
    tableau.append(True)
premiers = []
for i in range(2,limite,1):
    if tableau[i] == True :
        for j in range(i*i,limite,i):
            tableau[j] = False
for i in range(limite):
    if tableau[i] == True:
        premiers.append(i)
print(premiers)