#include <stdio.h>
#include <string.h>

int A();
int A_prime();
int B();

char expr[100];
int count, l;

int main()
{
    count = 0;

    printf("\nRecursive descent parsing for the following grammar\n");
    printf("\nA->aA'\nA'->AaB|b|B\nB->c|d\n");
    printf("\nEnter the string to be checked:");
    fgets(expr, 100, stdin);

    if (A())
    {
        if (expr[count] == '$')
            printf("\nString is accepted");
        else
            printf("\nString is not accepted");
    }
    else
    {
        printf("\nString not accepted");
    }

    return 0;
}

int A()
{
    // A->aA'

    if (expr[count] == 'a')
    {
        count++;
        if (A_prime())
        {
            return 1;
        }
        else
            return 0;
    }
    else
        return 0;
}

int A_prime()
{
    // A'->AaB|b|B
    if (A())
    {
        if (expr[count] == 'a')
        {
            count++;
            if (B())
                return 1;
            else
                return 0;
        }
        else
            return 0;
    }
    else if (expr[count] == 'b')
    {
        count++;
        return 1;
    }
    else if (B())
    {
        return 1;
    }
    else
    {
        return 1;
    }
}

int B()
{
    // B->c|d

    if (expr[count] == 'c')
    {
        count++;
        return 1;
    }
    else if (expr[count] == 'd')
    {
        count++;
        return 1;
    }
    else
        return 0;
}
