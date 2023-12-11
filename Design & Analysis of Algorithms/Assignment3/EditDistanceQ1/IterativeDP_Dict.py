def edit_distance_memo(row, col, memo, source, target):
    for r in range(1, row):
        for c in range(1, col):
            cost_del = memo[(r - 1, c)] + 1
            cost_insert = memo[(r, c - 1)] + 1
            if source[r - 1] == target[c - 1]:
                cost_main = memo[(r - 1, c - 1)]
                cost_subs = float('inf')
            else:
                cost_main = float('inf')
                cost_subs = memo[(r - 1, c - 1)] + 1
            memo[(r, c)] = min(cost_del, cost_insert, cost_main, cost_subs)
    return memo[(row - 1, col - 1)]


def main():
    source = "MATHS"
    target = "ARTS"
    row = len(source) + 1
    col = len(target) + 1

    # Initialize memoization dictionary
    memo = {(i, 0): i for i in range(row)}
    memo.update({(0, j): j for j in range(col)})

    # Print the initialized memoization dictionary
    print("Initialized Memoization Dictionary:")
    print(memo)
    print("\n")

    edit_distance_memo(row, col, memo, source, target)

    # Print the updated memoization dictionary
    print("Updated Memoization Dictionary:")
    print(memo)
    print("\nEdit distance:", memo[(row - 1, col - 1)])


if __name__ == '__main__':
    main()
