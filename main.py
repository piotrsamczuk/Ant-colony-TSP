import random

import networkx as nx
import matplotlib.pyplot as plt


def generateGraph(numOfNodes, weightRange=(1, 100)):
    graph = nx.complete_graph(numOfNodes)
    for i, j in graph.edges():
        graph.edges[i, j]["weight"] = random.randint(*weightRange)
    return graph


def plotNextGraphStep(graph, currentTour, currentNode, position):
    plt.clf()
    nx.draw(graph, position, with_labels=True, node_color="lightblue", node_size=600)
    pathEdges = list(zip(currentTour, currentTour[1:]))  # wizualizacja sciezki
    nx.draw_networkx_edges(
        graph, position, edgelist=pathEdges, edge_color="red", width=2
    )
    nx.draw_networkx_nodes(
        graph, position, nodelist=[currentNode], node_color="green", node_size=700
    )
    edgeLabels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, position, edge_labels=edgeLabels)
    plt.pause(1)


def calculateTourValue(graph, tour):
    return sum(graph[tour[i]][tour[i + 1]]["weight"] for i in range(len(tour) - 1))


# algorytm na potrzeby testow wizualizacji
def greedyTSP(graph, startNode=None):
    if startNode is None:
        startNode = random.choice(list(graph.nodes))

    position = nx.spring_layout(graph)
    plt.ion()
    plt.show()

    unvisited = set(graph.nodes)
    unvisited.remove(startNode)
    tour = [startNode]
    currentNode = startNode
    plotNextGraphStep(graph, tour, startNode, position)

    while unvisited:
        nextNode = min(
            unvisited, key=lambda node: graph[currentNode][node]["weight"]
        )  # nastepny node to ten, ktory ma najmniejsza wage/wartosc
        unvisited.remove(nextNode)
        tour.append(nextNode)
        currentNode = nextNode
        plotNextGraphStep(graph, tour, currentNode, position)

    tour.append(startNode)
    plotNextGraphStep(graph, tour, currentNode, position)
    print(tour)
    tourValue = calculateTourValue(graph, tour)
    print(f"wartosc podrozy: {tourValue}")
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    graph1 = generateGraph(5)
    greedyTSP(graph1, 0)
