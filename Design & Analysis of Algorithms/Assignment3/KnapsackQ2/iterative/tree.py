"""
    Pros:
        Allows for hierarchical representation.
        Useful for certain variations of the knapsack problem.
    Cons:
        More complex to implement.
        May not be as space-efficient for this specific problem.
        Traversing the binary tree can be time-consuming.
        Space complexity depends on the number of items selected.

    Time Complexity: O(2^n)
    Space Complexity: O(n)

A tree, while providing a hierarchical representation, 
may be overkill for this specific problem unless dealing with variations requiring a more complex structure.
"""


class Node:
    def __init__(self, value, is_kept, left=None, right=None):
        self.value = value
        self.is_kept = is_kept
        self.left = left
        self.right = right

def KnapSack(i, j, values, weights):
    if i == 0 or j == 0:
        return Node(0, 0)
    elif weights[i-1] > j:
        return KnapSack(i-1, j, values, weights)
    else:
        exclude_node = KnapSack(i-1, j, values, weights)
        include_node = KnapSack(i-1, j-weights[i-1], values, weights)
        
        # Create a new node for the included item
        new_include_node = Node(include_node.value + values[i-1], 1, include_node, None)
        
        # Compare the values of the new include node and the exclude node
        if new_include_node.value > exclude_node.value:
            return new_include_node
        else:
            return exclude_node

def print_selected_items(node, i, weights, values):
    if node is None:
        return
    if node.is_kept == 1:
        print(f"Item {i} (Weight: {weights[i-1]}, Value: {values[i-1]})")
    print_selected_items(node.left, i-1, weights, values)

def main():
    max_capacity = 11
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    row_n = len(values)

    print("Selected items: ")
    root = KnapSack(row_n, max_capacity, values, weights)
    print_selected_items(root, row_n-1, weights, values)

    print("\nMax worth of bag of {}: {}".format(max_capacity, root.value))

if __name__ == '__main__':
    main()
