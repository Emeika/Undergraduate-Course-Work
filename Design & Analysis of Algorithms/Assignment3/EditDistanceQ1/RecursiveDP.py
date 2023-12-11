def edit_distance(r, c, dp, source, target):
    if dp[r][c] == -1:
        if dp[r-1][c] == -1:
            cost_del = edit_distance(r-1, c, dp, source, target)  + 1 
        else:
            cost_del = dp[r-1][c]  + 1 
        
        if dp[r][c-1] == -1:
            cost_insert = edit_distance(r, c-1, dp, source, target)  + 1 
        else:
            cost_insert = dp[r][c-1]  + 1 

        if source[r-1] == target[c-1]:
            if dp[r-1][c-1] == -1:
                cost_main = edit_distance(r-1, c-1, dp, source, target)
            else:
                cost_main = dp[r-1][c-1]
        else:
            cost_main = float('inf')  # Handle non-matching case - large value

        if source[r-1] != target[c-1]:
            if dp[r-1][c-1] == -1:
                cost_subs = edit_distance(r-1, c-1, dp, source, target) + 1
            else:
                cost_subs = dp[r-1][c-1] + 1
        else:
            cost_subs = float('inf')  # Handle non-matching case 
        dp[r][c] = min(cost_del, cost_insert, cost_subs, cost_main)
        
    return dp[r][c]


def main():
    source = "intention"
    target = "execution"
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
    print("Original array:")
    for r in dp:
        print(r)

    print(f"\nEdit distance to convert {source} to {target}")

    edit_distance(row-1, col-1, dp, source, target)

    for r in dp:
        print(r)
    
    print("\nEdit distance:",dp[row - 1][col - 1])
    print("\n")

if __name__ == '__main__':
    main()




# Space complexity : O(mn)