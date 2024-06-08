def nearest_neighbor(distance_matrix):
    num_vertices = len(distance_matrix)
    visited = [False] * num_vertices
    current_vertex = 0
    visited[0] = True
    path = [0]
    total_distance = 0

    for _ in range(num_vertices - 1):
        min_distance = float('inf')
        nearest_vertex = None
        for next_vertex in range(num_vertices):
            if not visited[next_vertex] and distance_matrix[current_vertex][next_vertex] < min_distance:
                min_distance = distance_matrix[current_vertex][next_vertex]
                nearest_vertex = next_vertex
        path.append(nearest_vertex)
        total_distance += min_distance
        visited[nearest_vertex] = True
        current_vertex = nearest_vertex

    total_distance += distance_matrix[path[-1]][0]  # Dodanie odległości powrotu do punktu początkowego

    return path, total_distance
