class Graph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.graph = [[0 if (j == 0) or (i == 0) else -1 for i in range(cols)] for j in range(rows)]

    def add_edge(self, row, col, weight):
        self.graph[row][col] = weight

    def print_graph(self):
        for row in self.graph:
            print(row)

def edit_distance(row, col, graph, source, target):
    for r in range(1, row):
        for c in range(1, col):
            cost_del = graph.graph[r-1][c] + 1
            cost_insert = graph.graph[r][c-1] + 1
            if source[r-1] == target[c-1]:
                cost_main = graph.graph[r-1][c-1]
                cost_subs = float('inf')
            else:
                cost_main = float('inf')
                cost_subs = graph.graph[r-1][c-1] + 1
            graph.graph[r][c] = min(cost_del, cost_insert, cost_main, cost_subs)

def main():
    source = "MATHS"
    target = "ARTS"
    row = len(source) + 1
    col = len(target) + 1

    graph = Graph(row, col)

    counter_r = 0
    counter_c = 0

    for r in range(row):
        graph.graph[r][0] = counter_r
        counter_r += 1

    for c in range(col):
        graph.graph[0][c] = counter_c
        counter_c += 1

    # Print the initialized 2D array
    graph.print_graph()
    print("\n")

    edit_distance(row, col, graph, source, target)

    graph.print_graph()
    print("\nEdit distance:", graph.graph[row - 1][col - 1])


if __name__ == '__main__':
    main()
