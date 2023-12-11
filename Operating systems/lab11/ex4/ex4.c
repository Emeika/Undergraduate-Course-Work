#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Allocate memory for an integer
    int *arr = (int *)malloc(3 * sizeof(int));

    arr[4] = 42;
    free(arr);

    return 0;
}
