#include <vector>
#include <algorithm>
#include <iostream>

void merge(std::vector<int> &arr, int start, int mid1, int mid2, int end)
{
    std::vector<int> temp(end - start + 1);
    int temp1, temp2, range1, range2;
    int i = start, k = start, j = mid1 + 1, m = mid2 + 1, l = 0;

    while (i <= mid1 && j <= mid2 && m <= end)
    {
        if ((arr[i] <= arr[j]) && (arr[i] <= arr[m]))
        {
            temp[k++] = arr[i++];
        }
        else if ((arr[j] <= arr[i]) && (arr[j] <= arr[m]))
        {
            temp[k++] = arr[j++];
        }
        else if ((arr[m] <= arr[i]) && (arr[m] <= arr[j]))
        {
            temp[k++] = arr[m++];
        }
    } // one list gets exhausted

    if (i == mid1 + 1) // 1st list is exhausted
    {
        temp1 = j, range1 = mid2;
        temp2 = m, range2 = end;
    }

    if (j == mid2 + 1) // 2nd list is exhausted
    {
        temp1 = i, range1 = mid1;
        temp2 = m, range2 = end;
    }

    if (m == end + 1) // 3rd list is exhausted
    {
        temp1 = i, range1 = mid1;
        temp2 = j, range2 = mid2;
    }

    while (temp1 <= range1 && temp2 <= range2)
    { // 2 lists gets exhausted
        if (arr[temp1] <= arr[temp2])
        {
            temp[k++] = arr[temp1++];
        }
        else
        {
            temp[k++] = arr[temp2++];
        }
    }

    // Copy remaining elements of first list, if any
    while (temp1 <= range1)
    {
        temp[k++] = arr[temp1++];
    }

    // Copy remaining elements of second list, if any
    while (temp2 <= range2)
    {
        temp[k++] = arr[temp2++];
    }

    // Copy remaining elements of third list, if any
    while (m <= end)
    {
        temp[k++] = arr[m++];
    }

    for (i = start; i <= end; i++)
    {
        arr[i] = temp[i - start];
    }
}

// void threeWayMergeSort(std::vector<int> &arr, int start, int end)
// {
//     if (start < end)
//     {
//         int mid1 = start + (end - start) / 3;
//         int mid2 = start + 2 * (end - start) / 3 + 1;

//         threeWayMergeSort(arr, start, mid1);
//         threeWayMergeSort(arr, mid1 + 1, mid2);
//         threeWayMergeSort(arr, mid2 + 1, end);

//         merge(arr, start, mid1 + 1, mid2 + 1, end);
//     }
// }

void threeWayMergeSort(std::vector<int> &arr, int start, int end)
{
    if (end - start >= 2)
    {
        int mid1 = start + (end - start) / 3;
        int mid2 = start + 2 * (end - start) / 3;

        threeWayMergeSort(arr, start, mid1);
        threeWayMergeSort(arr, mid1 + 1, mid2);
        threeWayMergeSort(arr, mid2 + 1, end);

        merge(arr, start, mid1, mid2, end);
    }
    else if (start < end) // 2 elements left - sort and return
    {
        if (arr[start] > arr[end])
        {
            std::swap(arr[start], arr[end]);
        }
    }
}

int main()
{ // 8, 1, 5, 9, 2, 4
    std::vector<int> arr = {8, 1, 5, 9, 2, 4};
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
