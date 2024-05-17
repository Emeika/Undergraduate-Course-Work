import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def find_median(arr):
    sorted_arr = merge_sort(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        mid = n // 2
        median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        mid = n // 2
        median = sorted_arr[mid]

    return median


# Input list
numbers = [90, 8, 80, 30, 72, 49, 79, 56, 39, 42, 93, 10, 23, 78, 7, 98, 10, 80, 26, 95, 34, 96, 83, 13, 57, 50, 49, 32,
           82, 55, 69, 71, 10, 50, 31, 4, 89, 49, 99, 36, 46, 65, 46, 72, 33, 73, 49, 100, 23, 9]

# Measure execution time
start_time = time.time()

# Finding the median
median = find_median(numbers)

# Calculate execution time
execution_time = time.time() - start_time

print("Median:", median)
print("Execution time:", execution_time, "seconds")
