### Imports ### 
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from knn_refub import nearest_neighbor
from ant import generate_distance_matrix, ant_colony_optimization, calculate_distance

### Main ###
if __name__ == "__main__":

    # while True:
    #     num_cities_input = input("How many cities do you want to visit? --> ")
    #     try:
    #         num_cities = int(num_cities_input)
    #         if num_cities <= 0:
    #             print("Please enter a positive integer.")
    #         else:
    #             break  # Input is valid, exit the loop
    #     except ValueError:
    #         print("Please enter a valid integer.")

    #cities = generate_distance_matrix(num_cities)
    #np.save('50matrix.npy', cities)
    cities = np.load('50matrix.npy')


    # Using Nearest Neighbor to solve the TSP
    knn_visiting_order, knn_distance_traveled = nearest_neighbor(cities)
    print(f"BEST VISITING ORDER KNN: {knn_visiting_order}")
    print(f"DISTANCE TRAVELED KNN: {knn_distance_traveled}")

    # Using Ant Colony Optimization to solve the TSP
    num_ants = 30
    num_iterations = 100
    evaporation_rate = [0.3,0.5,0.8,1,2,4]
    alpha = 1
    beta = 10
    deta=[[0.3,0,0,0,0,0],[0.5,0,0,0,0,0],[0.8,0,0,0,0,0],[1,0,0,0,0,0],[2,0,0,0,0,0],[4,0,0,0,0,0]]
    sr = 0

    for i in range(6):
        sr=sr/5
        print('Wynik sredniej:')
        print(sr)
        sr = 0
        for j in range(5):
            print(evaporation_rate[i])
            start_time = time.time()
            best_path, best_distance = ant_colony_optimization(cities, num_ants, num_iterations,evaporation_rate[i], alpha, beta)
            #print("Best Path found by Ant Colony Optimization:", best_path)
            # Pomiar czasu zakończenia
            end_time = time.time()
            execution_time = end_time - start_time
            print("Distance Traveled by Ant Colony Optimization:", best_distance)
            print(f"Czas wykonania: {execution_time} sekund")
            row=i
            column=j+1
            deta[row][column]=execution_time
            sr=execution_time+sr

    print(deta)
    np.savetxt('deta', deta)
    sr = sr / 5
    print('WYNIK SREDNIEJ:')
    print(sr)
    # print("Best Path found by Ant Colony Optimization:", best_path)
    # print("Distance Traveled by Ant Colony Optimization:", best_distance)
    #
    # # Visualization using matplotlib
    # fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    #
    # # Plotting cities for KNN
    # axes[0].scatter(cities[:, 0], cities[:, 1], c='red', label='Cities')
    # axes[0].set_title('KNN TSP Path')
    #
    # # Plotting paths for KNN
    # knn_path_x = [cities[i][0] for i in knn_visiting_order]
    # knn_path_y = [cities[i][1] for i in knn_visiting_order]
    # axes[0].plot(knn_path_x + [knn_path_x[0]], knn_path_y + [knn_path_y[0]], 'b--', label='KNN Path')
    #
    # # Annotating cities for KNN
    # for i, city in enumerate(cities):
    #     axes[0].annotate(str(i), (city[0], city[1]))
    #
    # axes[0].set_xlabel('X Coordinate')
    # axes[0].set_ylabel('Y Coordinate')
    # axes[0].legend()
    # axes[0].grid(True)
    #
    # # Plotting cities for Ant Colony Optimization
    # axes[1].scatter(cities[:, 0], cities[:, 1], c='red', label='Cities')
    # axes[1].set_title('Ant Colony Optimization TSP Path')
    #
    # # Plotting paths for Ant Colony Optimization
    # ant_path_x = [cities[i][0] for i in best_path]
    # ant_path_y = [cities[i][1] for i in best_path]
    # axes[1].plot(ant_path_x + [ant_path_x[0]], ant_path_y + [ant_path_y[0]], 'g-', label='Ant Path')
    #
    # # Annotating cities for Ant Colony Optimization
    # for i, city in enumerate(cities):
    #     axes[1].annotate(str(i), (city[0], city[1]))
    #
    # axes[1].set_xlabel('X Coordinate')
    # axes[1].set_ylabel('Y Coordinate')
    # axes[1].legend()
    # axes[1].grid(True)
    #
    # plt.tight_layout()
    # plt.show()