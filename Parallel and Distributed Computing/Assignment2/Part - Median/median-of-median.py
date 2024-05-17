import multiprocessing
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
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

def median_of_medians(arr, i):
    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [merge_sort(sublist)[len(sublist)//2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = merge_sort(medians)[len(medians)//2]
    else:
        pivot = median_of_medians(medians, len(medians)//2)
    low = [j for j in arr if j < pivot]
    high = [j for j in arr if j > pivot]
    pivots = [j for j in arr if j == pivot]
    if i < len(low):
        return median_of_medians(low, i)
    elif i < len(low) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(high, i - len(low) - len(pivots))

def parallel_median_of_medians(arr):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        size = len(arr)
        result = pool.apply(median_of_medians, [arr, size//2])
    return result

if __name__ == '__main__':
    numbers = [90, 8, 80, 30, 72, 49, 79, 56, 39, 42, 93, 10, 23, 78, 7, 98, 10, 80, 26, 95, 34, 96, 83, 13, 57, 50, 49, 32,
               82, 55, 69, 71, 10, 50, 31, 4, 89, 49, 99, 36, 46, 65, 46, 72, 33, 73, 49, 100, 23, 9]
    start_time = time.time()
    median = parallel_median_of_medians(numbers)
    execution_time = time.time() - start_time
    print("Median:", median)
    print("Execution time:", execution_time, "seconds")
