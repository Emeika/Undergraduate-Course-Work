#include <iostream>
#include <cstdlib>  // to use Srand
using namespace std;

void DiceRoll(int& score)  // pass by reference
{
    score += rand() % 6+1; // randomly generates a number between 1 to 6
}

int main()
{
    int score, roll;
    srand(time(0));
    cout << "Enter the number: ";
    cin >> roll;
    for (int i = 0; i < roll; i++){  // Loop for roll dice the number of times the user enters
        DiceRoll(score);  // Roll the dice and add the score to the score variable
        cout << "Score: " << score << endl;  // Print the score to the screen
    }
    cout << "The score is: " << score;
}

