class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def print_graph(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")
        print("\n")


def edit_distance(row, col, dp, source, target, graph):
    for r in range(1, row):
        for c in range(1, col):
            cost_del = dp[(r - 1, c)] + 1
            cost_insert = dp[(r, c - 1)] + 1
            if source[r - 1] == target[c - 1]:
                cost_main = dp[(r - 1, c - 1)]
                cost_subs = float('inf')
            else:
                cost_main = float('inf')
                cost_subs = dp[(r - 1, c - 1)] + 1
            dp[(r, c)] = min(cost_del, cost_insert, cost_main, cost_subs)

            # Add edges to represent the graph
            if dp[(r, c)] == cost_del:
                graph.add_edge((r, c), (r - 1, c))
            if dp[(r, c)] == cost_insert:
                graph.add_edge((r, c), (r, c - 1))
            if dp[(r, c)] == cost_subs:
                graph.add_edge((r, c), (r - 1, c - 1))

    return dp[(row - 1, col - 1)]


def main():
    source = "MATHS"
    target = "ARTS"
    row = len(source) + 1
    col = len(target) + 1

    dp = {(i, 0): i for i in range(row)}
    dp.update({(0, j): j for j in range(col)})

    # Initialize the graph
    graph = Graph()

    print("Initialized adjacency list graph:")
    print(dp, "\n")

    ed = edit_distance(row, col, dp, source, target, graph)

    print("Updated adjacency list graph:")
    print(dp, "\n")
    print(f"Edit distance to convert {source} to {target}: {ed}")

    # Print the graph
    print("\nGraph (Adjacency List):")
    graph.print_graph()


if __name__ == '__main__':
    main()

# space complexity : O(n*m)
# Iterative dictionary uses a dictionary (dp) to represent a 2D table.
# Graph adjacency list uses a class-based approach with a dictionary (dp) and an adjacency list (adj_list) to represent a graph.
# Both codes are similar in terms of the core logic of calculating edit distance. 
# However the graph being used which makes it more space taking with extra edges/self causing more overhead