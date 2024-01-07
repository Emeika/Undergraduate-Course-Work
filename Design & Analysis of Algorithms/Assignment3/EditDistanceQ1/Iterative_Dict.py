def edit_distance(row, col, dp, source, target):
    for r in range(1, row):
        for c in range(1, col):
            cost_del = dp[(r - 1, c)] + 1
            cost_insert = dp[(r, c - 1)] + 1
            if source[r - 1] == target[c - 1]:
                cost_main = dp[(r - 1, c - 1)]
                cost_subs = float('inf')
            else:
                cost_main = float('inf')
                cost_subs = dp[(r - 1, c - 1)] + 1
            dp[(r, c)] = min(cost_del, cost_insert, cost_main, cost_subs)
    return dp[(row - 1, col - 1)]


def main():
    source = "MATHS"
    target = "ARTS"
    row = len(source) + 1
    col = len(target) + 1

    dp = {(i, 0): i for i in range(row)}
    dp.update({(0, j): j for j in range(col)})

    print("Initialized Dictionary:")
    print(dp, "\n")

    ed = edit_distance(row, col, dp, source, target)

    print("Updated Dictionary:")
    print(dp, "\n")
    print(f"\nEdit distance to convert {source} to {target}: {ed}")


if __name__ == '__main__':
    main()

# space complexity : O(n*m)