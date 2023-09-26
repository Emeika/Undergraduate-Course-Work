#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    int ans;
    int first = atoi(argv[1]);
    int second = atoi(argv[2]);
    char operator= argv[3][0];

    if (operator== '+')
    {
        ans = first + second;
    }
    else if (operator== '-')
    {
        ans = first - second;
    }
    else if (operator== '*')
    {
        ans = first * second;
    }
    else if (operator== '/')
    {
        ans = first / second;
    }
    printf("%d", ans);
}