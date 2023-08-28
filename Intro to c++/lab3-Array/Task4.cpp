#include <iostream>
using namespace std;

int main()
{
    int length, p;
    cout << "Enter the size of the array: ";
    cin >> length;
    int arr[length];  //Array made of given size
    for (int i = 0; i < length; i++) {  // Fill the array using loop by taking value from user
    cout << "Enter value: ";
    cin >> arr[i];
    }
    do {
        cout << "Enter +ve number of positions to shift right: ";
        cin >> p;
    }
    while (p < 0 || p > length);

    // move each element to the right p position 
    for (int i = 0; i < p; i++) {
        int temp = arr[length - 1];  // every element is stored in a temp variable to avoid loss of data after overriding 
        // Last p elements are moved to the beginning
        for (int j = length - 1; j > 0 ; j--){
            arr[j] = arr[j - 1];
        }
        arr[0] = temp;
    }

    // Display resulting array
    for (int x = 0; x < length; x++) {
        cout << arr[x] << " ";   
        
        
    }


    
}