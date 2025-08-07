## Exemple d'usage d'une matrice d'adjacence

A = [0,3,0,10,0,0,0,0]
B = [3,0,12,0,8,0,0,0]
C = [0,12,0,0,0,0,7,5]
D = [10,0,0,0,4,12,0,0]
E = [0,8,0,4,0,2,6,0]
F = [0,0,0,12,2,0,4,0]
G = [0,0,7,0,6,4,0,15]
H = [0,0,5,0,0,0,15,0]

graphe = [A,C,D,E,F,G,H]
utilisateurs = ["A","B","C","D","E","F","G","H"]

for i in range(len(graphe)):
    for j in range(len(graphe)):
        if graphe[i][j] != 0 and i != j:
            print(utilisateurs[i],"est ami avec",utilisateurs[j])
