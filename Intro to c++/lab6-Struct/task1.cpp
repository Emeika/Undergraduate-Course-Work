#include <iostream>
using namespace std;

//RationalNumber struct represents a fraction with a numerator (a) and a denominator (b)
struct RationalNumber {  
    int a; // numerator
    int b; // denominator
};

double toDouble(RationalNumber rn) {
    // static_cast used coz floating-point division is carried out instead of integer division. 
    //result will be a double value
    return static_cast<double>(rn.a) / rn.b; // Divide numerator with denominator

}

int main() {
    RationalNumber rn = {2, 3}; //create a RationalNumber struct
    cout << toDouble(rn) << endl; // prints 0.666667
    return 0;
}
