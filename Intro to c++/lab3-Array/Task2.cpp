#include <iostream>
using namespace std;

int main() 
{
    int length, val, first, last;
    cout << "Enter array length: ";  // Take size of input from user
    cin >> length;

    int * values = new int(length);  
    int n = sizeof(values)/sizeof(values[0]); // find the size of the array - how many elements it has
    for (int i = 0; i < length; i++) {  // Fill the array using loop by taking value from user
        cout << "Enter Value: ";
        cin >> val;
        values[i] = val;
    }

    first = values[0];  // First and last element stored
    last = values[length - 1];
    values[0] = last;   // Replace the first and last element
    values[length - 1] = first;
    cout << "The swapped array is: "<< endl;

    for (int x = 0; x < length; x++) {
        cout << values[x] << " ";   // Display all the elements in the array
        
        
    }
    

}


