#include <vector>
#include <algorithm>
#include <iostream>

void merge(std::vector<int> &arr, int start, int mid1, int mid2, int end)
{
    std::vector<int> temp(end - start + 1);
    int i = start, j = mid1, k = mid2, l = 0;

    while (i < mid1 && j < mid2 && k <= end)
    {
        if (arr[i] < arr[j])
        {
            if (arr[i] < arr[k])
            {
                temp[l++] = arr[i++];
            }
            else
            {
                temp[l++] = arr[k++];
            }
        }
        else
        {
            if (arr[j] < arr[k])
            {
                temp[l++] = arr[j++];
            }
            else
            {
                temp[l++] = arr[k++];
            }
        }
    }

    while (i < mid1 && j < mid2)
    {
        if (arr[i] < arr[j])
        {
            temp[l++] = arr[i++];
        }
        else
        {
            temp[l++] = arr[j++];
        }
    }

    while (j < mid2 && k <= end)
    {
        if (arr[j] < arr[k])
        {
            temp[l++] = arr[j++];
        }
        else
        {
            temp[l++] = arr[k++];
        }
    }

    while (i < mid1 && k <= end)
    {
        if (arr[i] < arr[k])
        {
            temp[l++] = arr[i++];
        }
        else
        {
            temp[l++] = arr[k++];
        }
    }

    while (i < mid1)
        temp[l++] = arr[i++];
    while (j < mid2)
        temp[l++] = arr[j++];
    while (k <= end)
        temp[l++] = arr[k++];

    for (i = start; i <= end; i++)
    {
        arr[i] = temp[i - start];
    }
}

void threeWayMergeSort(std::vector<int> &arr, int start, int end)
{
    if (end > start)
    {
        int mid1 = start + (end - start) / 3;
        int mid2 = start + 2 * (end - start) / 3 + 1;

        threeWayMergeSort(arr, start, mid1);
        threeWayMergeSort(arr, mid1 + 1, mid2);
        threeWayMergeSort(arr, mid2 + 1, end);

        merge(arr, start, mid1 + 1, mid2 + 1, end);
    }
}

int main()
{
    std::vector<int> arr = {8, 1, 5, 9, 2, 0};
    int n = arr.size();

    std::cout << "Original array: ";
    for (int i = 0; i < n; ++i)
        std::cout << arr[i] << " ";
    std::cout << std::endl;

    threeWayMergeSort(arr, 0, n - 1);

    std::cout << "Sorted array: ";
    for (int i = 0; i < n; ++i)
        std::cout << arr[i] << " ";
    std::cout << std::endl;

    return 0;
}
