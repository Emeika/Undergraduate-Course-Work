#include <iostream>
#include <string>
using namespace std;

struct StringStat {  // // Define a struct to hold string and stats data
    string s;
    // number of lower, uppercase and digit characters
    int lower = 0;   
    int upper = 0;
    int digit = 0;
};

int main() {
    const int SIZE = 5;
    StringStat stats[SIZE];

    // Read input strings and compute stats
    for (int i = 0; i < SIZE; i++) {
        cout << "Enter a string: ";
        cin >> stats[i].s;

        // Compute the stats for the input string
        for (char c : stats[i].s) {
            if (islower(c)) {
                stats[i].lower++;   // add 1 to lower if its lower
            } else if (isupper(c)) {
                stats[i].upper++;
            } else if (isdigit(c)) {
                stats[i].digit++;
            }
        }
    }

    // Print results
    cout << "\nResults:\n";
    for (int i = 0; i < SIZE; i++) {
        cout << "String #" << i+1 << ": " << stats[i].s << "\n";
        cout << "Lower case count: " << stats[i].lower << "\n";
        cout << "Upper case count: " << stats[i].upper << "\n";
        cout << "Digit count: " << stats[i].digit << "\n\n";
    }

    return 0;
}
