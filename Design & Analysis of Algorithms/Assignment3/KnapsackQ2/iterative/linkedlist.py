"""
    Pros:
        Can dynamically adjust size during runtime.
        Suitable if the number of items is not known in advance.
    Cons:
        Traversal might be slower compared to arrays.
        Space complexity depends on the number of items selected.

    Time Complexity: O(row_n * max_capacity)
    Space Complexity: O(row_n * max_capacity)
        
The space complexity of the linked list-based approach is higher than using a simple 2D array
A linked list might not be the most space-efficient choice, as it requires additional memory for pointers.

"""

class Node:
    def __init__(self, value=0, is_kept=0, next_node=None):
        self.value = value
        self.is_kept = is_kept
        self.next_node = next_node

class LinkedListDP:
    def __init__(self):
        self.head = None

    def get(self, i, j):
        current = self.head
        while current is not None:
            if current.value[0] == i and current.value[1] == j:
                return current.value[2], current.is_kept
            current = current.next_node
        return 0, 0

    def set(self, i, j, value, is_kept):
        new_node = Node(value=(i, j, value), is_kept=is_kept, next_node=self.head)
        self.head = new_node

    def print_table(self, row_n, max_capacity):
        for i in range(row_n + 1):
            for j in range(max_capacity + 1):
                value, is_kept = self.get(i, j)
                print(f"{value} K-{is_kept}", end="\t")
            print()


def initializeLinkedListDP(max_capacity):
    dp = LinkedListDP()
    # Initialize the first row
    for j in range(max_capacity + 1):
        dp.set(0, j, 0, 0)
    # Initialize the first column
    for i in range(1, max_capacity + 1):
        dp.set(i, 0, 0, 0)
    return dp

def KnapSack(row_n, max_capacity, values, weights, dp):
    for i in range(1, row_n + 1):
        for j in range(1, max_capacity + 1):
            exclude_item, exclude_item_is_kept = dp.get(i-1, j)
            if weights[i-1] > j:
                dp.set(i, j, exclude_item, 0)
            else:
                include_item, include_item_is_kept = dp.get(i-1, j-weights[i-1])
                include_item += values[i-1]
                if include_item > exclude_item:
                    dp.set(i, j, include_item, 1)
                else:
                    dp.set(i, j, exclude_item, 0)

    print("Selected items:")
    i, j = row_n, max_capacity
    while i > 0 and j > 0:
        _, is_kept = dp.get(i, j)
        if is_kept:
            print(f"Item {i} (Weight: {weights[i-1]}, Value: {values[i-1]})")
            j -= weights[i-1]
        i -= 1


def main():
    max_capacity = 11
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    row_n = len(values)
    
    # Initialize the linked list with base cases
    dp = initializeLinkedListDP(max_capacity)

    print("Selected items: ")
    KnapSack(row_n, max_capacity, values, weights, dp)
    print("\n")

    print("Dynamic Programming Table:")
    for c in range(max_capacity+1):
        print(f"W({c})\t", end=" ")
    print()
    dp.print_table(row_n, max_capacity)

    print("\n")

    print("Max worth of bag of {}: {}".format(max_capacity, dp.get(row_n, max_capacity)[0]))

if __name__ == '__main__':
    main()
