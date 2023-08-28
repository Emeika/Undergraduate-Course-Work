#include <iostream>
using namespace std;

int main() {  // Sir told to not take input for test case & DNA size chain & No. Corruption
    const int c = 5;   //Number of Corruptions
    char DNA[5][30] = {"adbcabcccccddacdcdcddcdacdabb",
                       "bsaasddbacadacdcdcddcdaccabca",
                       "abcdabbbccdcabcddbacccccccacd",
                       "bbddcdabdcaacdcdbacbccdbacada",
                       "bbddcdabdcaacdcdbacbccdbacada"};

    for (int x = 0; x < 5; x++) { //Outer loop to access each string in DNA
        bool isAffected = false; // Boolean to keep record of whether consecutive c is found 5 times
        for (int y = 0; y < 26; y++){  //inner loop to access each character of string
            if (DNA[x][y] == 'c' && DNA[x][y+1] == 'c' && DNA[x][y+2] == 'c' && DNA[x][y+3] == 'c' && DNA[x][y+4] == 'c'){
                isAffected = true;    // Condition to check if next 5 characters are the same as c
                break;   
            }
        }
        if (isAffected) {
            cout << "Affected\n";
        } else {
            cout << "Healthy\n";
        }
    }
    return 0;
}
