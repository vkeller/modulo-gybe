# Adjacency matrix representation of the graph
graph = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]

num_vertices = len(graph)
visited = [False] * num_vertices
distances = [float('inf')] * num_vertices
start_vertex = 0
distances[start_vertex] = 0

for _ in range(num_vertices):
    # Find the vertex with the minimum distance
    min_distance = float('inf')
    min_index = -1
    for v in range(num_vertices):
        if not visited[v] and distances[v] < min_distance:
            min_distance = distances[v]
            min_index = v

    visited[min_index] = True

    # Update distances for adjacent vertices
    for v in range(num_vertices):
        if graph[min_index][v] > 0 and not visited[v]:
            new_distance = distances[min_index] + graph[min_index][v]
            if new_distance < distances[v]:
                distances[v] = new_distance

# Output the shortest distances from the start vertex
print("Vertex Distance from Source")
for i in range(num_vertices):
    print(f"{i} \t\t {distances[i]}")