### Imports ### 
import numpy as np
import heapq as hq
import matplotlib.pyplot as plot

from knn import choose_knn_route
from knn_refub import nearest_neighbor
from knn_alt import solve_tsp_nearest

from ant import generate_distance_matrix, calculate_distance, ant_colony_optimization

### Main ###
if __name__ == "__main__":

    while True:
        num_cities_input = input("How many cities do you want to visit? --> ")
        try:
            num_cities = int(num_cities_input)
            if num_cities <= 0:
                print("Please enter a positive integer.")
            else:
                break  # Input is valid, exit the loop
        except ValueError:
            print("Please enter a valid integer.")

    #cities = generate_tsp_dataset(num_cities)
    cities=generate_distance_matrix(num_cities)

    # Using KNN to solve th TSP

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # code of below KNN is probably too real-accurate to our problem, we are in hypothetical situation, where
    # graph is square matrix with diagonal zeros. I suggest to use second algorithm, because its typical for matrixes
    # it will, or not- help us xD

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #knn_visiting_order2, knn_distance_traveled2 = choose_knn_route(cities, STARTING_CITY_INDEX)
    #print(f"BEST VISITING ORDER KNN ORG: {knn_visiting_order2}")
    #print(f"DISTANCE TRAVELED KNN ORG: {knn_distance_traveled2}")


    # knn_visiting_order, knn_distance_traveled = choose_knn_route(cities, STARTING_CITY_INDEX)
    knn_visiting_order, knn_distance_traveled = nearest_neighbor(cities)
    print(f"BEST VISITING ORDER KNN: {knn_visiting_order}")
    print(f"DISTANCE TRAVELED KNN: {knn_distance_traveled}")

    # Here we should solve it by ANT Algorithm
    num_ants = 10
    num_iterations = 100
    best_path, best_distance = ant_colony_optimization(cities, num_ants, num_iterations)
    print("Najlepsza trasa znaleziona przez algorytm mrówkowy:", best_path)
    print("Długość najlepszej trasy ACO:", best_distance)


    # Here we can compare the results
    ...

    # BETA VERSION #
    #visualize_cities(cities)  # TODO: connections beetween cities, maybe dynamic show during program execution?, better layout?
   
