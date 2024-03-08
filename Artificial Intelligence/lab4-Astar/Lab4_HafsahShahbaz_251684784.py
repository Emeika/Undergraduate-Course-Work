# Name: Hafsah Shahbaz
# Roll No.: 251684784

"""
Lab Task:

For this lab you will be implementing A* (A Star Search) on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable
with the functions

MAIN TASKS:

    1- Modify graph.py to have the ability to store heuristics
    2- Create a funciton 'get_h' in graph.py to get heuristic for a node : input will be a Node and output will be heuristic
    3- Create the graph in graph.py to and check all the functions
    4- Implement A* function

Your function should print the shortest path along with the cost of that path.
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph
from collections import deque


def a_star_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according
    to the A* Search Algorithm.

    NOTE: print the path and cost

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graphs
    :params goal_node: (String) goal node from the graph

    :return: None
    """
    queue = deque()
    queue.append(start_node)
    shortest_path = []
    min_cost = 0
    min_node = None
    final_cost = 0

    visited = set()

    while queue:
        node = queue.pop()
        shortest_path.append(node)

        if node == goal_node:
            break

        for neighbour in graph.neighbours(node):
            if neighbour not in visited:
                visited.add(neighbour)

                edge_cost = graph.get_cost(node, neighbour)
                h_cost = graph.get_h(neighbour)
                total_cost = edge_cost + h_cost

                if min_cost == 0 or total_cost < min_cost:
                    min_cost = total_cost
                    min_node = neighbour
                    min_edge = edge_cost

        queue.append(min_node)
        final_cost += min_edge
        min_cost = 0
        min_node = None

    print("Shortest Path:", shortest_path)
    print("Cost:", final_cost)


if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {'A': ['B', 'C'],
                   'B': ['C', 'E'],
                   'C': ['G'],
                   'G': [],
                   'E': ['G'],
                   'D': ['B', 'E'],
                   'S': ['A', 'D'],
                   }

    # setting up connection costs
    graph.weights = {
        'AC': 10, 'AB': 5,
        'BC': 2, 'BE': 1,
        'CG': 4,
        'SA': 3, 'SD': 2,
        'DB': 1, 'DE': 4,
        'EG': 3
    }
    # setting up heuristics
    graph.heuristics = {
        'A': 9,
        'B': 4,
        'C': 2,
        'D': 5,
        'E': 3,
        'G': 0,
        'S': 7
    }

    a_star_search(graph, 'S', 'G')
