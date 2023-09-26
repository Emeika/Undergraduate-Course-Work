/*
Write a gcc C program: compile and run in Ubuntu. Create an array "zeta" of size 30 that holds floating point numbers.
The first 3 elements are 1.1, 2.2, 3.3. The nth element is calculated using the expression:
zeta(n)=0.5*zeta(n-3)+ 0.3*zeta(n-2)+ 0.2*zeta(n-1) (a)
Use a loop to print the complete array of 30 elements, each value separated by comma.
On the next line of the output, the program should print only the numbers in the array that have odd integer part.
(The integer part of the number 123.456 is 123.)
[ure]
Hint: Equation (a) is an iterative formula introduced in the course Discrete Maths.
These formulas take in the values from previous iterations to give new values. For example the zeta (10) would be:
zeta (10)=0.5*zeta (7)+ 0.3*zeta (8)+ 0.2*zeta(9

*/

#include <stdio.h>

int main()
{
    float zeta[30] = {1.1, 2.2, 3.3};

    for (int n = 3; n < 30; n++)
    {
        zeta[n] = 0.5 * zeta[n - 3] + 0.3 * zeta[n - 2] + 0.2 * zeta[n - 1];
    }

    for (int i = 0; i < 30; i++)
    {
        printf("%.2f", zeta[i]);
        if (i != 29)
        {
            printf(",");
        }
    }

    printf("\nOdd numbers: \n");

    for (int i = 0; i < 30; i++)
    {
        int intValue = (int)zeta[i]; // Convert float to int
        if (intValue % 2 == 1)
        {
            printf("%d", intValue);
            if (i != 29)
            {
                printf(",");
            }
        }
    }
}