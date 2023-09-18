// Comp 301-B
// Hafsah Shahbaz
// 251684784
// 9/18/2023

#include <stdio.h>

int main()
{
    int list[7] = {29, 31, 32, 22, 20, 20, 19};
    // int list[7] = {29, 28, 30, 22, 20, 40, 19};

    int index = -1;
    int check = 0;

    for (int i = 0; i < 7; i++)
    {

        if (list[i] >= list[i + 1])
        {

            index = check;
        }
        else
        {
            // If there's a rise or no change, reset index
            index = -1;
            check = i + 1;
        }
    }

    if (index == -1)
    {
        printf("%d\n", index);
    }
    else
    {
        printf("The temperature starts dropping continuously at index %d.\n", index);
    }

    return 0;
}

/*

int list[28] = {29, 31, 30, 22, 20, 20, 19,
                27, 26, 33, 29, 31, 30, 22,
                32, 29, 28, 27, 22, 33, 29,
                31, 30, 22, 22, 29, 28, 27};


*/