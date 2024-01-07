"""
    Pros:
        Provides key-value pairs for easy identification of objects.
        Efficient for looking up values.
    Cons:
        May consume more memory due to key-value overhead.

    Space complexity is O(row_n * max_capacity).
    Time complexity is O(row_n * max_capacity)

"""

def KnapSack(row_n, max_capacity, values, weights, dp, items):
    for i in range(1, row_n + 1):
        for j in range(1, max_capacity + 1):
            exclude_item = dp[i - 1, j]
            if weights[i - 1] > j:
                dp[i, j] = exclude_item
            else:
                include_item = values[i - 1] + dp[i - 1, j - weights[i - 1]]
                dp[i, j] = max(exclude_item, include_item)
                if include_item > exclude_item:
                    items[i, j] = i

def print_selected_items(dp, items, row_n, max_capacity, weights, values):
    i, j = row_n, max_capacity
    selected_items = []
    while i > 0 and j > 0:
        if items[i, j] != 0:
            selected_items.append(items[i, j] - 1)
            j -= weights[items[i, j] - 1]
        i -= 1

    print("Selected items:")
    for item in selected_items[::-1]:
        print(f"Item {item + 1}: Weight {weights[item]}, Value {values[item]}")

def main():
    max_capacity = 11
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    row_n = len(values)
    dp = {(i, 0): 0 for i in range(max_capacity + 1)}
    dp.update({(0, j): 0 for j in range(max_capacity + 1)})
    items = {(i, j): 0 for i in range(row_n + 1) for j in range(max_capacity + 1)}

    # Print the initialized 2D array
    print("Original array:")
    print(dp, "\n")
    print("\n")

    KnapSack(row_n, max_capacity, values, weights, dp, items)

    print("Updated array:")
    print(dp, "\n")

    print(f"\nMax worth of bag of {max_capacity}: {dp[row_n, max_capacity]}")

    print_selected_items(dp, items, row_n, max_capacity, weights, values)

if __name__ == '__main__':
    main()
