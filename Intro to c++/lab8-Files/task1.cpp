#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int num = 0;
    cout << "Enter num: ";
    cin >> num;
    ofstream fout; // open file for writing
    fout.open("multiplicationTable.text");
    for (int i = 1; i <= num; i++)
    { // Starts a loop for iterating over rows, from 1 to num.
        for (int j = 1; j <= num; j++)
        {                         // Starts a nested loop for iterating over columns, from 1 to num.
            fout << i * j << " "; // Writes the product of i and j to the file, followed by a space
        }
        fout << endl;
    }

    fout.close();
}