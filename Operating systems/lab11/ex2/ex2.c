#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Allocate memory for an array of integers
    int *arr = (int *)malloc(5 * sizeof(int));

    if (arr == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < 5; i++)
    {
        arr[i] = i * 10;
    }

    // Use the allocated memory
    for (int i = 0; i < 5; i++)
        printf("arr[%d] = %d\n", i, arr[i]);

    // Free the allocated memory
    free(arr);

    return 0;
}
