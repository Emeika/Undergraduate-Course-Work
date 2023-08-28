#include <iostream>
using namespace  std;

int main() {
    int first_value = 5;
    int second_value = 15;
    int *p1, *p2;

    p1 = &first_value; // p1 = address of first value
    p2 = &second_value; // p2 = address of second value
    *p1 = 10;                   // value pointed by p1 = 10
    *p2 = *p1;                   // value pointed by p2 = value pointed by p1
    p1 = p2;                     // p1 = p2 (address of pointer is copied)
    *p1 = 20;                    // value pointed by p1 = 20

    // print first value, second value
    cout << "First value: " <<  first_value << "\nSecond value: " << second_value;       


}
