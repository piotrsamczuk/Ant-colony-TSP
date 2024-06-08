### Imports ###
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from knn_refub import nearest_neighbor
from ant import generate_distance_matrix, ant_colony_optimization, calculate_distance

# Function to plot the TSP graph and path
def plot_tsp(ax, cities, path, title, color='blue', last_city_highlighted=True):
    ax.scatter(cities[:, 0], cities[:, 1], c=color, label='Cities')

    # Drawing edges of the path
    for i in range(len(path) - 1):
        start_city = cities[path[i]]
        end_city = cities[path[i + 1]]
        ax.plot([start_city[0], end_city[0]], [start_city[1], end_city[1]], color=color)

    # Adding the line closing the path
    start_city = cities[path[-1]]
    end_city = cities[path[0]]
    ax.plot([start_city[0], end_city[0]], [start_city[1], end_city[1]], color=color, linestyle='--')

    # Highlighting the last city in red
    if last_city_highlighted:
        last_city = cities[path[-1]]
        ax.scatter(last_city[0], last_city[1], color='red', s=100, label='Last city')

    for i, city in enumerate(cities):
        ax.annotate(str(i), (city[0], city[1]))

    ax.set_title(title)
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.legend()
    ax.grid(True)

### Main ###
if __name__ == "__main__":
    num_cities = 20
    # cities = generate_distance_matrix(num_cities)
    # np.save(f'{num_cities}matrix.npy', cities)
    cities = np.load(f'preGeneratedCities/{num_cities}matrix.npy')

    # Using Nearest Neighbor to solve the TSP
    knn_visiting_order, knn_distance_traveled = nearest_neighbor(cities)
    print(f"BEST VISITING ORDER KNN: {knn_visiting_order}")
    print(f"DISTANCE TRAVELED KNN: {knn_distance_traveled}")

    # Using Ant Colony Optimization to solve the TSP
    num_ants = 15
    num_iterations = 100
    evaporation_rate = 1
    alpha = 1
    beta = 5
    deta = [[0.3, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0], [0.8, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0]]
    sr = 0

    for i in range(6):
        sr = sr / 5
        print('Wynik średniej:')
        print(sr)
        sr = 0
        for j in range(5):
            print(evaporation_rate)
            start_time = time.time()
            best_path, best_distance = ant_colony_optimization(cities, num_ants, num_iterations, evaporation_rate, alpha, beta)
            end_time = time.time()
            execution_time = end_time - start_time
            print("Distance Traveled by Ant Colony Optimization:", best_distance)
            print(f"Czas wykonania: {execution_time} sekund")
            row = i
            column = j + 1
            deta[row][column] = execution_time
            sr = execution_time + sr

    print(deta)
    np.savetxt('deta', deta)
    sr = sr / 5
    print('WYNIK ŚREDNIEJ:')
    print(sr)
    print("Best Path found by Ant Colony Optimization:", best_path)
    print("Distance Traveled by Ant Colony Optimization:", best_distance)

    # Visualization using matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Plotting cities and paths for KNN
    plot_tsp(axes[0], cities, knn_visiting_order, 'KNN TSP Path', color='blue')

    # Plotting cities and paths for Ant Colony Optimization
    plot_tsp(axes[1], cities, best_path, 'Ant Colony Optimization TSP Path', color='green')

    plt.tight_layout()
    plt.show()
