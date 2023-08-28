#include <iostream>

using namespace std;

int matrix_size; // declaring matrix_size as a global variable

void Input(int **matrix) {
    // taking input from the user for the matrix
    for (int i = 0; i < matrix_size; i++) {
        for (int j = 0; j < matrix_size; j++) {
            cin >> matrix[i][j];
        }
    }
}

void Display(int **matrix) {
    // displaying the matrix
    for (int i = 0; i < matrix_size; i++) {   // Loop through the rows
        for (int j = 0; j < matrix_size; j++) {   // Loop through the columns
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}


void reverseDiagonal(int **matrix) {
    // Loop over the rows in the top half of the matrix
    for (int i = 0; i < matrix_size / 2; i++) {
        // Swap the element at position (i,i) with its counterpart on the opposite diagonal
        //The first swap for 1st diagonal at (0,0) and (n-1,n-1) 
        int temp = matrix[i][i];
        matrix[i][i] = matrix[matrix_size - i - 1][matrix_size - i - 1];
        matrix[matrix_size - i - 1][matrix_size - i - 1] = temp;

        // Swap the element at position (i,n-i-1) with its counterpart on the opposite diagonal
        // First Swap for 2nd diagonal at (0,n-1) and (n-1,0)
        temp = matrix[i][matrix_size - i - 1];
        matrix[i][matrix_size - i - 1] = matrix[matrix_size - i - 1][i];
        matrix[matrix_size - i - 1][i] = temp;
    }
}

int main() {
    cout << "Enter the matrix_size of the square matrix: ";
    cin >> matrix_size;
    if (matrix_size <= 0) {  // Make sure input is a positive integer 
        do {
            cout << "Invalid matrix_size entered. Please enter a positive integer.\n";
            cin >> matrix_size;
        }
        while (matrix_size <= 0);
    }
    // Declare a pointer to a pointer of type int, and allocate memory 
    // for 'matrix_size' number of pointers.
    int **matrix = new int*[matrix_size];
    // Initialize the array by allocating memory for each row 
    //in the matrix with 'matrix_size' number of columns.
    for (int i = 0; i < matrix_size; i++) {
        matrix[i] = new int[matrix_size];
    }

    cout << "Enter the elements of the matrix:" << endl;
    Input(matrix);

    cout << "Matrix before reversing diagonals:" << endl;
    Display(matrix);

    reverseDiagonal(matrix);

    cout << "Matrix after reversing diagonals:" << endl;
    Display(matrix);

    // deallocating memory
    for (int i = 0; i < matrix_size; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}
