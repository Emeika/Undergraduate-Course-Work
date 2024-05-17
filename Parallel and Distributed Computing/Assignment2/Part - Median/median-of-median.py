import multiprocessing
import math


def median_of_medians(arr, i):

    # Divide arr into sublists of len 5
    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        # The pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)//2)

    # Partitioning step
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
    # Input list
    numbers = [90, 8, 80, 30, 72, 49, 79, 56, 39, 42, 93, 10, 23, 78, 7, 98, 10, 80, 26, 95, 34, 96, 83, 13, 57, 50, 49, 32,
               82, 55, 69, 71, 10, 50, 31, 4, 89, 49, 99, 36, 46, 65, 46, 72, 33, 73, 49, 100, 23, 9]

    # Finding the median
    median = parallel_median_of_medians(numbers)
    print("Median:", median)
