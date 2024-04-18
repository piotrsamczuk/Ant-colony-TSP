"""
    *KNN ALGORITHM CODE*
    
"""

### Imports ### 
import numpy as np
import heapq as hq

### Costants ###
CONSIDERED_NEIGHBOURS = 2

### Functions ###
def calculate_distance(p1, p2):
    distance = 0

    if len(p1) != len(p2):
        raise ValueError("Uneven number of points dimensions")
    else:
        # Euclidean distance equation
        for i in range(len(p1)):
          distance += (p1[i] - p2[i])**2
    
    return np.sqrt(distance)

def find_neighbours(database_array, search_indexes, new_point, k_neighbors):

    if len(database_array) == 0:
        raise ValueError("Database is empty")
    if k_neighbors < 1:
        raise ValueError("k_neighbours must be > 1")
    if len(new_point) != len(database_array[0]):
        raise ValueError("Not enough point parameters")

    # Ensuring the seatch will not exceed the range
    if len(search_indexes) < k_neighbors:
        k_neighbors = len(search_indexes)

    # Calculating all distances and storing them at the heap
    distances = []
    for i in search_indexes:
        distance = round(calculate_distance(database_array[i], new_point), 2)
        hq.heappush(distances, (distance, i))

    # Appending k nearest neighbours from stack in ascending order
    neighbors = []
    for _ in range(k_neighbors):

       distance, index = hq.heappop(distances)
       neighbors.append((distance, index))

    return neighbors

# Chooses the next city to visit based on a KNN 2-depth approach.
def choose_next_city(current_city, cities, search_indexes, k_neighbors):

    next_city_index = None
    min_distance = np.inf  # Initialize with infinity for comparison
    distance_traveled = None

    # Find nearest neighbor (excluding current city)
    neighbors = find_neighbours(cities, search_indexes, cities[current_city], k_neighbors + 1)[1:]  # Skip nearest (current) city

    for i in neighbors:
        nb_distance = i[0]
        nb_index = i[1]
        neighbor_nearest_neighbour = find_neighbours(cities, search_indexes, cities[nb_index], 2)[1:]  # Skip nearest (current) city
        # Adding the second level nnnb distance
        nb_distance += neighbor_nearest_neighbour[0][0]
        if nb_distance < min_distance:
            min_distance = nb_distance
            next_city_index = nb_index
            distance_traveled = i[0]

    return next_city_index, distance_traveled

# Does the whole knn-based route search and returns it's ORDER and DISTANCE
def choose_knn_route(cities, start):
    distance_traveled = 0
    visiting_order = [start] # Stores indexes by visiting order
    unvisited_cities = [] # Stores indexes of unvisited cities

    for i in range(len(cities)):
        unvisited_cities.append(i)

    # For Debug
    # print(cities)
    # print(unvisited_cities)

    for i in range(len(cities) - 1):
        next_city, distance = choose_next_city(start, cities, unvisited_cities, CONSIDERED_NEIGHBOURS)
        distance_traveled += distance
        visiting_order.append(next_city)
        unvisited_cities = [element for element in unvisited_cities if element != next_city]
        print(cities)
        print(unvisited_cities)

    return visiting_order, distance_traveled
