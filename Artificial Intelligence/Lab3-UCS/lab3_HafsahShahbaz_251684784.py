# Name: Hafsah Shahbaz
# Roll: 251684784

"""
Lab Task:

For this lab you will be implementing Uniform Cost Search on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable
with the functions

MAIN TASK:
The graph provided has already been created below and the UCS (Unifrom cost search) function has been called.
You are suppose to fill in the UCS function declared below. A description of what the function should do is mentioned.
Use functions from the helper classes in order to write the UCS function.
Your function should print the shortest path along with the cost of that path.
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph
from custom_queue import PriorityQueue


def uniform_cost_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according
    to the Uniform Cost Search Algorithm.

    NOTE: print the path and cost

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graph
    :params goal_node: (String) goal node from the graph

    :return : None
    """
    frontier = PriorityQueue()
    frontier.insert(start_node, 0)
    visited = set()
    cost_so_far = {start_node: 0}
    path_to_node = {start_node: [start_node]}

    while not frontier.is_empty():
        _, current = frontier.remove()
        if current == goal_node:
            break
        visited.add(current)
        for next_node in graph.neighbours(current):
            if next_node not in visited:
                new_cost = cost_so_far[current] + \
                    graph.get_cost(current, next_node)
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost
                    frontier.insert(next_node, priority)
                    path_to_node[next_node] = path_to_node[current] + \
                        [next_node]

    path = path_to_node[goal_node]
    print("Shortest Path:", ','.join(path))
    print("Cost:", cost_so_far[goal_node])


if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        'A': set(['B', 'D']),
        'B': set(['A', 'E', 'C']),
        'C': set(['B', 'E', 'G']),
        'D': set(['A', 'E', 'F']),
        'E': set(['B', 'C', 'D', 'G']),
        'F': set(['D', 'G']),
        'G': set(['F', 'E', 'C'])
    }

    # setting up connection costs
    graph.weights = {
        'AB': 5, 'AD': 3,
        'BA': 5, 'BE': 4, 'BC': 1,
        'CB': 1, 'CE': 6, 'CG': 8,
        'DA': 3, 'DE': 2, 'DF': 2,
        'EB': 4, 'EC': 6, 'ED': 2, 'EG': 4,
        'FD': 2, 'FG': 3,
        'GF': 3, 'GE': 4, 'GC': 8
    }

    uniform_cost_search(graph, 'A', 'G')
    """
    the above statement should result in the following:

    Shortest Path: A,D,F,G
    Cost: 8
    """
