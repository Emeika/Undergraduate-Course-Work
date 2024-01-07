"""
    Pros:
        Useful for certain types of dynamic programming.
        Can be used for breadth-first search approaches.
    Cons:
        May not be as space-efficient as other structures. and making it more complex
    Time Complexity: O(row_n * max_capacity)
    Space Complexity: O(row_n * max_capacity)

"""

from collections import deque

def knapsack(row_n, max_capacity, values, weights, dp, keep):
    if weights[row_n-1] > max_capacity:
        if dp[row_n - 1][max_capacity] == -1:
            dp[row_n][max_capacity] = knapsack(
                row_n - 1, max_capacity, values, weights, dp, keep)
        return dp[row_n][max_capacity]

    else:
        if dp[row_n - 1][max_capacity] == -1:
            dp[row_n][max_capacity] = knapsack(row_n - 1, max_capacity, values, weights, dp, keep)

        if dp[row_n - 1][max_capacity - weights[row_n-1]] == -1:
            dp[row_n - 1][max_capacity - weights[row_n-1]] = knapsack(row_n - 1, max_capacity - weights[row_n-1], values, weights, dp, keep)

        without_current_item = dp[row_n - 1][max_capacity]
        with_current_item = values[row_n-1] + dp[row_n - 1][max_capacity - weights[row_n-1]]

        if with_current_item > without_current_item:
            keep[row_n][max_capacity] = 1
        dp[row_n][max_capacity] = max(without_current_item, with_current_item)
        return dp[row_n][max_capacity]

def main():
    # initialize data and queue
    max_capacity = 11
    values = [1, 6, 18, 22, 28]
    weights = [1, 2, 5, 6, 7]
    row_n = len(values)

    # using deque as a queue
    dp = [deque([-1] * (max_capacity + 1)) for _ in range(row_n + 1)]
    keep = [deque([0] * (max_capacity + 1)) for _ in range(row_n + 1)]

    # filling of base rows
    for i in range(max_capacity + 1):
        dp[0][i] = 0

    # filling of base cols
    for j in range(row_n + 1):
        dp[j][0] = 0

    # Call the knapsack function
    max_worth = knapsack(row_n, max_capacity, values, weights, dp, keep)

    # Print the updated array
    print("Updated array: \n")
    for c in range(max_capacity + 1):
        print(f"W({c}) ", end=" ")

    print()
    for r in dp:
        for c in r:
            if c != -1:
                print(c, "   ", end=" ")
            else:
                print("     ", end=" ")
        print()

    print(f"\nMax worth of bag of {max_capacity}: {max_worth}")

    # Print the selected items
    print("\nSelected items:")
    w = max_capacity
    for i in range(row_n, 0, -1):
        if keep[i][w] == 1:
            print(f"Item {i} (Weight: {weights[i-1]}, Value: {values[i-1]})")
            w -= weights[i-1]

if __name__ == '__main__':
    main()
