def merge_sort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2

        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)

        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    temp_arr = [0] * (end - start + 1)

    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(len(temp_arr)):
        arr[start + i] = temp_arr[i]


# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
