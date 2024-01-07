"""    Pros:
        Suitable for iterative solutions.
        Can be implemented using arrays or linked lists.
    Cons:
        Limited in terms of efficient random access.

    Time Complexity: O(row_n * max_capacity)
    Space Complexity: O(max_capacity)
    
A stack may not be the best choice as it lacks efficient random access, 
which is essential for the dynamic programming approach used in the 0/1 knapsack algorithm.

"""
def KnapSack(row_n, max_capacity, values, weights):
    dp = [0] * (max_capacity + 1)
    for i in range(1, row_n + 1):
        new_dp = dp.copy()
        for w in range(max_capacity + 1):
            if weights[i - 1] <= w:
                new_dp[w] = max(dp[w], values[i - 1] + dp[w - weights[i - 1]])
        dp = new_dp

    final_value = dp[max_capacity]
    selected = selected_items(dp, weights, row_n, max_capacity)

    return final_value, selected


def selected_items(dp, weights, row_n, max_capacity):
    selected = []
    i, w = row_n, max_capacity

    while i > 0 and w > 0:
        if dp[w] != dp[w - 1]:
            selected.append(i)
            w -= weights[i - 1]
            i -= 1
        else:
            i -= 1

    return selected


def main():
    # Initialize data
    max_capacity = 11
    values = [0, 1, 6, 18, 22, 28]
    weights = [0, 1, 2, 5, 6, 7]
    row_n = len(values) -1


    final_value, selected = KnapSack(row_n, max_capacity, values, weights)

    print(f"\nMax worth of bag of {max_capacity}: {final_value}")
    for i in selected:
        print(f"Item {i} (Weight: {weights[i-1]}, Value: {values[i-1]})")


if __name__ == '__main__':
    main()

