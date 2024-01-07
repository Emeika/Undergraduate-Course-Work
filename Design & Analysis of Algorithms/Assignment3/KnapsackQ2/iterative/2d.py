"""    Pros:
        Efficient for dynamic programming solutions.
        Easy to implement and understand.
    Cons:
        Consumes more space compared to some other structures.

    Space complexity is O(n * capacity).
    Time complexity is O(n * capacity).
a 2-D matrix is the most efficient choice.

"""
def KnapSack(row_n, max_capacity, values, weights, dp, items):
    for i in range(1, row_n + 1):
        for j in range(1, max_capacity + 1):
            exclude_item = dp[i-1][j]
            if weights[i-1] > j:
                dp[i][j] = exclude_item
            else:
                include_item = values[i-1] + dp[i-1][j-weights[i-1]]
                if include_item > exclude_item:
                    dp[i][j] = include_item
                    items[i][j] = i  # Keep track of the selected item
                else:
                    dp[i][j] = exclude_item


def print_selected_items(dp, items, row_n, max_capacity, weights, values):
    i, j = row_n, max_capacity
    selected_items = []
    while i > 0 and j > 0:
        if items[i][j] != 0:
            selected_items.append(items[i][j] - 1)
            j -= weights[items[i][j] - 1]
        i -= 1

    print("Selected items:")
    for item in selected_items[::-1]:
        print(f"Item {item + 1}: Weight {weights[item]}, Value {values[item]}")



def main():
    max_capacity = 11
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    row_n = len(values)
    dp = [[0 if (j == 0) or (i == 0) else -1 for j in range(max_capacity + 1)] for i in range(row_n + 1)]
    items = [[0 for _ in range(max_capacity + 1)] for _ in range(row_n + 1)]

    # Print the initialized 2D array
    print("Original array:")
    for r in dp:
        print(r)
    print("\n")

    KnapSack(row_n, max_capacity, values, weights, dp, items)

    print("Updated array:")
    for r in dp:
        print(r)

    print(f"\nMax worth of bag of {max_capacity}: {dp[row_n][max_capacity]}")

    print_selected_items(dp, items, row_n, max_capacity, weights, values)


if __name__ == '__main__':
    main()
