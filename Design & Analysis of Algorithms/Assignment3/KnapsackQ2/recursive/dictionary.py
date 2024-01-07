class Item:
    def __init__(self, cost=0, is_kept=0):
        self.cost = cost
        self.is_kept = is_kept

def KnapSack(row_n, max_capacity, values, weights, dp, items):
    if (row_n, max_capacity) not in dp:
        if weights[row_n-1] > max_capacity:
            dp[(row_n, max_capacity)] = KnapSack(row_n-1, max_capacity, values, weights, dp, items)
        else:
            include_item = values[row_n-1] + KnapSack(row_n-1, max_capacity - weights[row_n-1], values, weights, dp, items)
            exclude_item = KnapSack(row_n-1, max_capacity, values, weights, dp, items)
            dp[(row_n, max_capacity)] = max(include_item, exclude_item)
            if dp[(row_n, max_capacity)] == include_item:
                items[row_n-1].is_kept = 1  # Mark the item as selected
    return dp[(row_n, max_capacity)]

def main():
    max_capacity = 11
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    row_n = len(values)
    items = [Item(cost=values[i], is_kept=0) for i in range(row_n)]

    # Initialize the base case in dp
    dp = {(i, 0): 0 for i in range(row_n+1)}
    dp.update({(0, j): 0 for j in range(max_capacity+1)})

    
    print("Initialized Dictionary:")
    print(dp, "\n")
    KnapSack(row_n, max_capacity, values, weights, dp, items)

    print("Updated Dictionary:")
    print(dp, "\n")
    print("\nItems selected:")
    for i, item in enumerate(items):
        if item.is_kept:
            print(f"Item {i+1} (Weight: {weights[i]}, Value: {values[i]})")

    print(f"\nMax worth of bag of {max_capacity}: {dp[(row_n, max_capacity)]}")

if __name__ == '__main__':
    main()
