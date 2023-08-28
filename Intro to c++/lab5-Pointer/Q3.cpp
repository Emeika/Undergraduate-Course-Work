#include <iostream>
using namespace std;

int * DoubleIt(int *A , const int size){
    int new_size = 2 * size;
    int *B = new int[new_size];     // creating a new dynamic array with double the size of arr
    for(int i = 0; i < new_size; i++){
        if (i < size) {
            B[i] = 0;      // initializing the first half of array with 0s
        }
        else {
            B[i] = A[i - size];  // copying the contents of A to the second half of B
        }
    }
    return B;    // returning the pointer to the new dynamic array

}

int main() {
    int size = 0;
    cout << "Enter size of the array: ";
    cin >> size;

    int *A = new int[size];

    srand(0);
    for (int i = 0; i < size; i++){
        A[i] = rand() % 10;     //Filling the array with random nums (0-9)
    }
    cout << "Array before doubling: " << endl;
    for (int i = 0; i < size; i++){
        cout << A[i] << " ";
    }
    cout << endl;

    int *B = DoubleIt(A, size);
    cout << "Array after doubling: " << endl;
    for (int i = 0; i < (size *2); i++){
        cout << B[i] << " ";
    }
    cout << endl;
    delete[] A; // deallocating memory of array
    delete[] B;
}