/*
Compute the asymptotic complexity of the following
iterative code fragment to its closed form. Solve to find asymptotically tighter bounds.
Clearly show your working throughout.
*/

#include <iostream>
#include <cmath>

void Func1(int n)
{
    for (int t = 2; t ^ (5 / 2 + 2 / 5) <= n; t++)
    {
        std::cout << "Pakistan!";
    }
}
// ( n^10/29 -2 )
// O(n^10/29)  ?

void Func2(int n)
{
    for (int i = 1; i < n; i++)
    { // n-1
        for (int j = 1; j <= i ^ 3; j++)
        { // i^3
            for (int k = 1; k <= 2000; k++)
            { // 2000
                std::cout << "Pakistan";
            }
        }
    }
}

// 2nd iteration :use sum of cubes formula
//  n-1 * n^4 *1
// 0(n^5)  ?

void Func3(int n, int m)
{
    for (int i = n / 7; i >= 1; i--)
    { // n/7
        for (int j = 1; j <= log(3 / 2) * m; j++)
        { // log(3/ 2) *m
            std::cout << "Pakist                                                                                an";
        }
    }
}
// (n/7 * log3/2 m)
// O(nlogm )

void Func4(int n)
{
    for (int i = n / 3; i < n * n; i++)
    { // n^2 -n/3 -1
        for (int j = 1; j <= n / 4; j = j * sqrt(n))
        { // log(sqrtn) (n/4)
            for (int k = 1; k <= n; k = k * 3.5)
            { // log3.5 n
                std::cout << "Pakistan!";
            }
        }
    }
}

// (n^2  * log(n) * log(n))
// O(n^2 * (log(n))^2)
int main()
{
    int n = 10; // Assuming n is initialized to some value.
    int m = 20; // Assuming m is initialized to some value.

    Func2(n);    // 0(n^5)
    Func4(n);    // O(n^2 * (log(n))^2)
    Func1(m);    // O(n^10/29)
    Func3(n, m); // O(nlogm )

    return 0;
}
