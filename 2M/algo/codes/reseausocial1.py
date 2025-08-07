## Exemple d'usage d'une matrice d'adjacence
## Si la position i vaut 1, alors il y a un lien

utilisateurs = ["Alice","Bob","Carole","David","Eve","Mallory","Oscar","Trudy"]

Alice   = [0,1,0,1,0,0,0,0]
Bob     = [1,0,1,0,1,0,0,0]
Carole  = [0,1,0,0,0,0,1,1]
David   = [1,0,0,0,1,1,0,0]
Eve     = [0,1,0,1,0,1,1,0]
Mallory = [0,0,0,1,1,0,1,0]
Oscar   = [0,0,1,0,1,1,0,1]
Trudy   = [0,0,1,0,0,0,1,0]

graphe = [Alice,Carole,David,Eve,Mallory,Oscar,Trudy]

for i in range(len(graphe)):
    for j in range(len(graphe)):
        if graphe[i][j] != 0 and i != j:
            print(utilisateurs[i],"est ami avec",utilisateurs[j])

