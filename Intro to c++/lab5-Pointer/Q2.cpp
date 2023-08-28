#include <iostream>
using namespace std;
void swapAcrossCenter(int *arr, const int arr_len){
    for (int x = 0; x < arr_len/2; x++){   // We only need to iterate until the middle of the array
        int left = arr[x];
        int right = arr[arr_len - x - 1];  //The last un swapped value
        arr[x] = right;
        arr[right] = left;       // the rightmost swapped with the left most
    }
}


int main() {
    int arr_len = 5;
    int * arr = new int[arr_len];   // allocating memory for dynamic array with size 5
    for (int i = 0; i < arr_len; i++) {
        arr[i] = i;            // Filling the array with 0 to 4
    }

    cout << "Before function call: " << endl;
    for (int p = 0; p < arr_len; p++) {
        cout << arr[p] << " ";
    }
    cout << endl;

    swapAcrossCenter(arr, arr_len);
    // Printing the array
    cout << "After function call :" << endl;
    for (int j = 0; j < arr_len; j++){
        cout << arr[j] << " ";
    }

    delete[] arr; // deallocating memory of dynamic array

}