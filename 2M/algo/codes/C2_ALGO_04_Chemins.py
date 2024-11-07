# Code permettant de calculer l'algorithme de Dijkstra
# sur le graphe du cours C2_ALGO_04
import random

INF = 100000
nbr = 8

A = [ 0, 3, 0,10, 0, 0, 0, 0]
B = [ 3, 0,12, 0, 8, 0, 0, 0]
C = [ 0,12, 0, 0, 0, 0, 7, 5]
D = [10, 0, 0, 0, 4,12, 0, 0]
E = [ 0, 8, 0, 4, 0, 2, 6, 0]
F = [ 0, 0, 0,12, 2, 0, 4, 0]
G = [ 0, 0, 7, 0, 6, 4, 0,15]
H = [ 0, 0, 5, 0, 0, 0,15, 0]


graph = [A,B,C,D,E,F,G,H]

# Nomme le sommet à partir duquel on calcule l'arbre couvrant
premier = 2

noeuds = ["A","B","C","D","E","F","G","H"]
peres = [-1,-1,-1,-1,-1,-1,-1,-1]

nbr = len(graph)
visites = [False] * nbr
distances = [INF] * nbr
distances[premier] = 0

for i in range(nbr):
    # Recherche des noeuds avec la distance minimum
    min_distance = INF
    min_index = -1
    for v in range(nbr):
        if not visites[v] and distances[v] < min_distance:
            min_distance = distances[v]
            min_index = v

    # Calcul du père
#    for v in range(nbr):
#        if visites[v] == True:
#            peres[i] = v

    visites[min_index] = True

    # Recalcul des distances depuis le noeud
    for v in range(nbr):
        if graph[min_index][v] > 0 and not visites[v]:
            new_distance = distances[min_index] + graph[min_index][v]
            if new_distance < distances[v]:
                distances[v] = new_distance


#print(peres)


print("Distance depuis la source :",noeuds[premier])
print("Noeud","\t","Distance")
for i in range(nbr):
    print(noeuds[i],"\t",distances[i])


