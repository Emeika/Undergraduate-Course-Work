#include <iostream>
using namespace std;

int sum_of_digits(int num)
{
    int sum = 0;   // Declare sum is 0 to begin with
    while (num > 0)  // Loop runs until the num can no longer be divided
    {
        sum += num % 10;  // % 10 gets the last digit which gets added to sum
        num /= 10;    // Num is divided by 10 to get all but the last digit
    }
    return sum;
}

int main()
{
    int num;
    cout << "Enter number to get the sum of its digits: ";
    cin >> num;
    cout << "Sum of digits of " << num << " is " << sum_of_digits(num);
}