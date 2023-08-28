#include <iostream>
using namespace std;


int countOnes(int num)
{
    int ones = 0;
    while (num > 0) {
        if ((num % 2) == 1) {  // get the remainder and add to one if the remainder =1
            ones++; 
        }
        num = num / 2;  // Integer division until num can no longer be divided(num>0)
    }
    return ones;
}

int main()
{
    int num;
    cout << "Enter the decimal number: ";
    cin >> num;
    cout << "The number of ones in " << num << " is " << countOnes(num);
}
