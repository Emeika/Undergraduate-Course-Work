# Name: Hafsah Shahbaz
# Roll NO.:

"""
Lab Task:

For this lab you will be implementing Breadth First on a graph.

For this lab you are provided with one helper classes.
It is for making a graph.
You may open then the file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable
with the functions

MAIN TASK:
The graph provided has already been created below and the DFS (Breadth First Search) function has been called.
You are suppose to fill in the DFS function declared below. A description of what the function should do is mentioned.
Use functions from the helper class in order to write the UCS function.
Your function should print the path.
"""

# importing helper classes
from graph import Graph
from collections import deque


def breadth_first_search(graph, start_node):
    """
    The function should take in the graph defined along with the
    start node and print out the path according
    to the Breadth First Search Algorithm.

    NOTE: print the path

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graph

    :return : None
    """

    # write your code below

    visited = set()
    queue = deque([start_node])
    while queue:
        current = queue.popleft()
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            neighbours = graph.neighbours(current)
            for neighbour in neighbours:
                queue.append(neighbour)


if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        'A': ['B', 'D'],
        'B': ['A', 'E', 'C'],
        'C': ['B', 'E', 'G'],
        'D': ['A', 'E', 'F'],
        'E': ['B', 'C', 'D', 'G'],
        'F': ['D', 'G'],
        'G': ['F', 'E', 'C']
    }

    breadth_first_search(graph, 'A')
