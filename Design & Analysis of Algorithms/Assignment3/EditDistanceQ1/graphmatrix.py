class Graph:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.rows = len(source) + 1
        self.cols = len(target) + 1
        self.graph = [[0 if (j == 0) or (i == 0) else -1 for i in range(self.cols)] for j in range(self.rows)]
        self.edges = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.initialize_vertices()

    def initialize_vertices(self):
        for r in range(self.rows):
            self.graph[r][0] = r

        for c in range(self.cols):
            self.graph[0][c] = c

    def add_edge(self, u, v):
        # Add edges to represent the graph
        # This implementation assumes u and v are tuples representing positions in the matrix
        # Connect u to v by storing v in the adjacency matrix
        if self.edges[v[0]][v[1]] == -1:
            # If the cell contains -1, set it to a list containing the current edge
            self.edges[v[0]][v[1]] = [u]
        else:
            # If the cell already contains a list, append the current edge to the list
            self.edges[v[0]][v[1]].append(u)

    def print_edges(self):
        print("\nEdges in the Graph:")
        for r in range(self.rows):
            for c in range(self.cols):
                if self.edges[r][c] != -1:
                    for edge in self.edges[r][c]:
                        print(f"Edge from {edge} to ({r}, {c})")
        print("\n")

    def print_graph(self):
        for row in self.graph:
            print(row)
        print("\n")

def edit_distance(graph):
    for r in range(1, graph.rows):
        for c in range(1, graph.cols):
            cost_del = graph.graph[r-1][c] + 1
            cost_insert = graph.graph[r][c-1] + 1
            if graph.source[r-1] == graph.target[c-1]:
                cost_main = graph.graph[r-1][c-1]
                cost_subs = float('inf')
            else:
                cost_main = float('inf')
                cost_subs = graph.graph[r-1][c-1] + 1
            graph.graph[r][c] = min(cost_del, cost_insert, cost_main, cost_subs)

            # Add edges to represent the graph
            if graph.graph[r][c] == cost_del:
                graph.add_edge((r, c), (r - 1, c))
            if graph.graph[r][c] == cost_insert:
                graph.add_edge((r, c), (r, c - 1))
            if graph.graph[r][c] == cost_subs:
                graph.add_edge((r, c), (r - 1, c - 1))
    
    return graph.graph[r -1][c -1]

def main():
    source = "MATHS"
    target = "ARTS"

    graph = Graph(source, target)
    print("Initialized adjacency matrix graph:")
    graph.print_graph()

    ed = edit_distance(graph)

    print("Updated adjacency matrix graph:")
    print(f"Edit distance to convert {source} to {target} : {ed}")
    graph.print_graph()

    graph.print_edges()

if __name__ == '__main__':
    main()
