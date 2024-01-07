def edit_distance(row, col, dp, source, target):
    for r in range(1,row):
        for c in range(1, col):
            cost_del = dp[r-1][c]  + 1
            cost_insert = dp[r][c-1]  + 1
            if source[r-1] == target[c-1]:
                cost_main = dp[r-1][c-1]
                cost_subs = float('inf')  # Handle non-matching case 
            else:
                cost_main = float('inf')
                cost_subs = dp[r-1][c-1] + 1
            dp[r][c] = min(cost_del, cost_insert, cost_main, cost_subs)
    return dp[row - 1][col - 1]

def main():
    source = "MATHS"
    target = "ARTS"
    row = len(source) +1
    col = len(target) +1
    counter_r = 0
    counter_c = 0
    dp = [[0 if (j == 0) or (i == 0) else -1 for i in range(col)] for j in range(row)]

    for r in range(row):
        dp[r][0] = counter_r
        counter_r += 1

    for c in range(col):
        dp[0][c] = counter_c
        counter_c += 1

    # Print the initialized 2D array
    for r in dp:
        print(r)

    print("\n")

    edit_distance(row, col, dp, source, target)

    for r in dp:
        print(r)
    print("\nEdit distance:", dp[row - 1][col - 1])


if __name__ == '__main__':
    main()


# space complexity : O(n*m)
