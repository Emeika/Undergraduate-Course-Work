#include <stdio.h>

int add(int *arr, int size)
{
    int total = 0;
    for (int i = 0; i < size; i++)
    {
        total = total + arr[i];
    }
    return total;
}

int main()
{
    int size = 5;
    int arr[5] = {1, 2, 3, 4, 5};
    int total = add(arr, size);
    printf("total = %d\n", total);
}