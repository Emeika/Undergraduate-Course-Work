# Task 2
def count(list, num, total):
    if list == []:
        return total
    elif list[0] == num:
        total += 1

    return count(list[1:], num, total)
    return total

total = 0
print(count([5, 8, 5], 5, total))

# o(n)