#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Allocate memory for an integer
    int *ptr = (int *)malloc(sizeof(int));

    if (ptr == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Memory leak: forgetting to free the allocated memory
    // Comment out the following line to avoid the memory leak
    free(ptr);

    return 0;
}
