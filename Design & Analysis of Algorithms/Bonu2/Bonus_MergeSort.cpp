/*
HAFSAH SHAHBAZ
251684784
COMP303 - B
*/

#include <iostream>

void merge(int arrA[], int start, int div1, int div2, int end)
{
    int tempArr[end - start + 1];

    int i = start;
    int j = div1;
    int k = div2;
    int l = 0;

    while ((i < div1) && (j < div2) && (k <= end))
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

    while (i < div1 && j < div2)
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

    while (j < div2 && k <= end)
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

    while (i < div1 && k <= end)
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

    while (i < div1)
        tempArr[l++] = arrA[i++];

    while (j < div2)
        tempArr[l++] = arrA[j++];

    while (k <= end)
        tempArr[l++] = arrA[k++];

    for (i = start; i <= end; i++)
    {
        arrA[i] = tempArr[i - start];
    }
}

void mergeSort(int arrA[], int start, int end)
{
    if (start < end)
    {
        int div1 = start + (end - start) / 3;
        int div2 = start + 2 * (end - start) / 3;

        mergeSort(arrA, start, div1);
        mergeSort(arrA, div1 + 1, div2);
        mergeSort(arrA, div2 + 1, end);
        merge(arrA, start, div1, div2, end);
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
