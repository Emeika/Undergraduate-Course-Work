# Name: Hafsah Shahbaz
# Roll NO.: 251684784

class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {}  # dictionary of edges NODE: NEIGHBOURS

    def neighbours(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.
        :params node: (string) a node in the graph
        :return: (set) neighbouring nodes
        """

        return self.edges[node]

    def print(self):
        for node in self.edges:
            print(node, ":", self.edges[node])


if __name__ == "__main__":
    # testing out the graph class
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
    graph.print()
