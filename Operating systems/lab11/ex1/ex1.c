#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Allocate memory for an integer
    int *ptr = (int *)malloc(sizeof(int));

    *ptr = 42;
    printf("Value at allocated memory: %d\n", *ptr);

    free(ptr);

    return 0;
}
