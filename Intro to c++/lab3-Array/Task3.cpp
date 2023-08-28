#include <iostream>
#include <string>
using namespace std;

int main() {
    string inp;
    int i = 0;   //Counter to get the index value
    cout<< "Enter string: ";
    getline(cin, inp);    //Getline to store the string with spaces in a single variable
    for (char c : inp) {
        if (isalpha(c)) {   // Check if its a letter
            if (islower(c)) {
                cout<<"Character " << c << " at index[" << i <<"] is lower case alphabet\n";
            }
            else {
                cout<<"Character " << c << " at index[" << i <<"] is upper case alphabet\n";
            }
        
        }
        else if (isspace(c)) {   //Check if its a space character
            cout<<"Character " << c << " at index[" << i <<"] is a space\n";
        }
        else {     // Remaining are considered invalid
            cout<<"Character " << c << " at index[" << i <<"] is not a valid english alphabet\n";
        }
        i++;
    }
    return 0;
}