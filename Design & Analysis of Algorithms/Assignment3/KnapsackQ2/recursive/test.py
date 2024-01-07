def KnapSack(row_n, max_capacity, values, weights, dp):
    if weights[row_n-1] > max_capacity:
        if dp[row_n-1][max_capacity] == -1:
            cost_prev = KnapSack(row_n-1, max_capacity, values, weights, dp)
        else:
            cost_prev = dp[row_n-1][max_capacity]

        dp[row_n][max_capacity] = cost_prev
        return dp[row_n][max_capacity]
    else:
        if dp[row_n-1][max_capacity] == -1:
            exclude_item = KnapSack(row_n-1, max_capacity, values, weights, dp)
        else:
            exclude_item = dp[row_n-1][max_capacity]

        if dp[row_n-1][max_capacity - weights[row_n-1]] == -1:
            include_item = KnapSack(row_n-1, max_capacity - weights[row_n-1], values, weights, dp)
        else:
            include_item = dp[row_n-1][max_capacity - weights[row_n-1]]

        dp[row_n][max_capacity] = max(exclude_item, (values[row_n-1] + include_item) )

        return dp[row_n][max_capacity]

def main():
    max_capacity = 11
    weights = [1,2,5,6,7]
    values = [1,6,18,22,28]
    row_n = len(values)
    dp = [[0 if (j == 0) or (i == 0) else -1 for i in range(max_capacity +1)] for j in range(row_n +1)]

    # Print the initialized 2D array
    print("Original array:")
    for r in dp:
        print(r)
    print("\n")

    KnapSack(row_n, max_capacity, values, weights, dp)
    print("Updated array: \n")
    for c in range(max_capacity+1):
        print(f"W({c}) ", end=" ")

    print()
    for r in dp:
        for c in r:
            if c != -1:
                print(c, "   ", end=" ")
            else:
                print("     ", end=" ")
        print()

    print(f"\nMax worth of bag of {max_capacity}: {dp[row_n][max_capacity]}")

if __name__ == '__main__':
    main()