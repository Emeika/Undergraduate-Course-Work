class Graph:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.rows = len(source) + 1
        self.cols = len(target) + 1
        self.graph = [[0 if (j == 0) or (i == 0) else -1 for i in range(self.cols)] for j in range(self.rows)]
        self.initialize_vertices()

    def initialize_vertices(self):
        for r in range(self.rows):
            self.graph[r][0] = r

        for c in range(self.cols):
            self.graph[0][c] = c

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

if __name__ == '__main__':
    main()

# space complexity : O(n*m)
# In both cases, the 2D list is used to represent a matrix where each element [r][c] 
# stores the edit distance value for the corresponding substrings of the source and target strings.
# Iterative 2d code uses a 2D list (dp) to represent the dynamic programming table for edit distance.
# Iterative graph adjacency matrix uses a class (Graph) with a 2D list (graph) as an attribute to represent the adjacency matrix.
# Thus there isn't much difference between them other than the graph being used which makes it more space
# taking with extra edges/self causing more overhead