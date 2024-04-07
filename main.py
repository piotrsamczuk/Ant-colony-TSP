### Imports ### 
import numpy as np
import heapq as hq
import matplotlib.pyplot as plot

from knn import choose_knn_route

### Costants ###
STARTING_CITY_INDEX = 0

# Generate random city coordinates 
def generate_tsp_dataset(num_cities, arg_range = 1000):
  
  # List of two-dimensional tuples
  cities = np.random.randint(0, arg_range, (num_cities, 2))

  return cities

def visualize_cities(cities):
    # Scatter plot for a sample of cities
    plot.subplot(1, 1, 1)
    for i, city in enumerate(cities):
        plot.scatter(city[0], city[1], marker='o', color='b')
        plot.annotate(str(i), (city[0], city[1]), textcoords="offset points", xytext=(0, 10), ha='center')
    plot.xlabel('X-Coordinate')
    plot.ylabel('Y-Coordinate')
    plot.title(f'{len(cities)} Cities')
    plot.tight_layout()
    plot.show()

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

    cities = generate_tsp_dataset(num_cities)

    # Using KNN to solve th TSP 
    knn_visiting_order, knn_distance_traveled = choose_knn_route(cities, STARTING_CITY_INDEX)
    print(f"BEST VISITING ORDER: {knn_visiting_order}")
    print(f"DISTANCE TRAVELED: {knn_distance_traveled}")

    # Here we should solve it by ANT Algorithm
    ...

    # Here we can compare the results
    ...

    # BETA VERSION #
    visualize_cities(cities)  # TODO: connections beetween cities, maybe dynamic show during program execution?, better layout?
   
