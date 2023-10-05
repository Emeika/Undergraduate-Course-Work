/*
HAFSAH SHAHBAZ
251684784
COMP303 - B
*/

#include <iostream>

void merge(int arrA[], int p, int mid1, int mid2, int r)
{
    int tempArr[r - p + 1];

    int i = p;
    int j = mid1;
    int k = mid2;
    int l = 0;

    while ((i < mid1) && (j < mid2) && (k <= r))
    {
        if (arrA[i] < arrA[j])
        {
            if (arrA[i] < arrA[k])
            {
                tempArr[l++] = arrA[i++];
            }
            else
            {
                tempArr[l++] = arrA[k++];
            }
        }
        else
        {
            if (arrA[j] < arrA[k])
            {
                tempArr[l++] = arrA[j++];
            }
            else
            {
                tempArr[l++] = arrA[k++];
            }
        }
    }

    while (i < mid1 && j < mid2)
    {
        if (arrA[i] < arrA[j])
        {
            tempArr[l++] = arrA[i++];
        }
        else
        {
            tempArr[l++] = arrA[j++];
        }
    }

    while (j < mid2 && k <= r)
    {
        if (arrA[j] < arrA[k])
        {
            tempArr[l++] = arrA[j++];
        }
        else
        {
            tempArr[l++] = arrA[k++];
        }
    }

    while (i < mid1 && k <= r)
    {
        if (arrA[i] < arrA[k])
        {
            tempArr[l++] = arrA[i++];
        }
        else
        {
            tempArr[l++] = arrA[k++];
        }
    }

    while (i < mid1)
        tempArr[l++] = arrA[i++];

    while (j < mid2)
        tempArr[l++] = arrA[j++];

    while (k <= r)
        tempArr[l++] = arrA[k++];

    for (i = p; i <= r; i++)
    {
        arrA[i] = tempArr[i - p];
    }
}

void mergeSort(int arrA[], int p, int r)
{
    if (p < r)
    {
        int mid1 = p + (r - p) / 3;
        int mid2 = p + 2 * (r - p) / 3;

        mergeSort(arrA, p, mid1);
        mergeSort(arrA, mid1 + 1, mid2);
        mergeSort(arrA, mid2 + 1, r);
        merge(arrA, p, mid1, mid2, r);
    }
}

int main()
{
    int arrA[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arrA) / sizeof(arrA[0]);

    std::cout << "Original array: ";
    for (int i = 0; i < size; i++)
    {
        std::cout << arrA[i] << " ";
    }
    std::cout << std::endl;

    mergeSort(arrA, 0, size - 1);

    std::cout << "Sorted array: ";
    for (int i = 0; i < size; i++)
    {
        std::cout << arrA[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
