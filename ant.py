"""
    *ANT COLONY ALGORITHM CODE*
    IT IS STANDALONE FOR ANT
    MUST TO BE CONNECTED WITH MAIN
"""

import numpy as np
import itertools
#from python_tsp.exact import solve_tsp_dynamic_programming
#from python_tsp.heuristics import solve_tsp_simulated_annealing




# Generowanie macierzy odpowiadającej grafowi, po przekątnej zera, kolumna X i wiersz Y muszą odpowiadać kolumnie Y i
# wierszowi X bo to praktycznie jest macierzowo interpretowany graf
def generate_distance_matrix(num_vertices):
    distance_matrix = np.zeros((num_vertices, num_vertices))
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            distance_matrix[i][j] = distance_matrix[j][i] = np.random.randint(1, 100)  # losowanie odległości
    return distance_matrix

# Algorytm mrówkowy

#Alfa- waga dla feromonów Beta- Waga dla heurystyki.
def ant_colony_optimization(distance_matrix, num_ants, num_iterations, evaporation_rate=0.5, alpha=4, beta=7): #dane z książki, jeszcze do testów
    num_vertices = len(distance_matrix)
    pheromone_matrix = np.ones((num_vertices, num_vertices))  # macierz feromonów jako same jedynki
    best_path = None
    best_distance = np.inf

    for _ in range(num_iterations):
        # Przechowuje trasę każdej mrówki i jej dystans
        ant_paths = []
        ant_distances = []

        # Przechodzenie każdej mrówki
        for _ in range(num_ants):
            current_vertex = np.random.randint(num_vertices)  # początkowy wierzchołek dla mruwki randomizowany
            visited_vertices = [current_vertex]
            total_distance = 0

            # Budowanie trasy mrówki
            while len(visited_vertices) < num_vertices:
                unvisited_vertices = []
                for vertex in range(num_vertices):
                    if vertex not in visited_vertices:
                        unvisited_vertices.append(vertex)

                probabilities = []
                for next_vertex in unvisited_vertices:
                    pheromone_factor = (pheromone_matrix[current_vertex][next_vertex]) ** alpha #wpływ feromonów, wzór feromony na ścieżce x ^ alfa
                    distance_factor = (1 / distance_matrix[current_vertex][next_vertex]) ** beta #wpływ heurystyki, wzór 1/heurystyka dla ścieżki x ^beta
                    probabilities.append(pheromone_factor * distance_factor)  #po prostu mnożymy xd

                total_probability = sum(probabilities) #suma dla n dostepnych lokalizacji

                if total_probability == 0:
                    # Jeśli suma probabilities wynosi zero, równomiernie rozdziel szanse
                    probabilities = [1 / len(unvisited_vertices)] * len(unvisited_vertices)
                else:
                    probabilities = [prob / total_probability for prob in probabilities]
                    #ostateczny wzór z książki, tutaj mamy iloraz iloczynu
                    #pheromance i distance przez sumę tego iloczynu

                next_vertex = np.random.choice(unvisited_vertices, p=probabilities)


                # Dodanie odległości do kosztu trasy
                total_distance += distance_matrix[current_vertex][next_vertex]

                # Zaktualizowanie listy odwiedzonych wierzchołków
                visited_vertices.append(next_vertex)
                current_vertex = next_vertex

            # Wrócenie do punktu początkowego
            total_distance += distance_matrix[current_vertex][visited_vertices[0]]
            ant_paths.append(visited_vertices)
            ant_distances.append(total_distance)

            # Aktualizacja najlepszej trasy
            if total_distance < best_distance:
                best_distance = total_distance
                best_path = visited_vertices

        # Aktualizacja macierzy feromonów. Feromon to Feromon * Współczynnik parowania (??? sprawdzić poprawną pisownię)
        pheromone_matrix *= (1 - evaporation_rate)
        for path in ant_paths:
            for i in range(num_vertices - 1):
                #zagnieżdżone pętle, aktualizacja
                pheromone_matrix[path[i]][path[i+1]] += 1 / ant_distances[ant_paths.index(path)]
            pheromone_matrix[path[-1]][path[0]] += 1 / ant_distances[ant_paths.index(path)]

    return best_path, best_distance


def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i+1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Dodanie odległości powrotu do punktu początkowego
    return total_distance


# Przykładowe użycie
#num_vertices = 30  # liczba wierzchołków
#distance_matrix = generate_distance_matrix(num_vertices)
#print("Macierz odległości:")
#print(distance_matrix)


#permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
#print("Najlepsza trasa:", permutation)
#print("Długość najlepszej trasy:", distance)

#permutation1, distance1 = solve_tsp_simulated_annealing(distance_matrix)
#print("Najlepsza trasa:", permutation1)
#print("Długość najlepszej trasy:", distance1)


#num_ants = 10
#num_iterations = 100
#best_path, best_distance = ant_colony_optimization(distance_matrix, num_ants, num_iterations)
#print("Najlepsza trasa znaleziona przez algorytm mrówkowy:", best_path)
#print("Długość najlepszej trasy ACO:", best_distance)
