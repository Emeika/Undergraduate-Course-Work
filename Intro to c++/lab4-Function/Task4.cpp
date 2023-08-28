#include <iostream>
#include <string>
using namespace std;

void getJudgeData(double &score1, double &score2, double &score3, double &score4, double &score5)   //Reference paramater
{
    
    double temp;
    for (int i = 1; i <= 5; i++){   // Loop to take input 5 times from 5 Judges 
        do {
            cout << "Enter the score of judge " << i << " : ";
            cin >> temp;    //Temporary variable to take multiple inputs for different judges and to store it respectively in the score variable
        } while ((temp < 0) || (temp > 10));   // Loop to validate if the score is between 0 and 10
        
        if (i == 1) score1 = temp;   // stores in the score variable for which it was entered 
        else if (i == 2) score2 = temp;   // If judge 2 is entering score so temp input is stored in score2
        else if (i == 3) score3 = temp;
        else if (i == 4) score4 = temp;
        else if (i == 5) score5 = temp;

        
    }

}


int findLowest(double &score1, double &score2, double &score3, double &score4, double &score5)
{
    double min = score1;   // Min gets replaced with the lowest score by comparing it with every score
    if (score2 < min) {    // if its less than the current minimum value then it gets replaced
        min = score2;
    }
    if (score3 < min) {
        min = score3;
    }
    if (score4 < min) {
        min = score4;
    }
    if (score5 < min) {
        min = score5;
    }
    return min;
}

int findHighest(double &score1, double &score2, double &score3, double &score4, double &score5)
{
    double max = score1;    // Same logic like min  
    if (score2 > max) {      // if its greater than the current maximum value then it gets replaced
        max = score2;
    }
    if (score3 > max) {
        max = score3;
    }
    if (score4 > max) {
        max = score4;
    }
    if (score5 > max) {
        max = score5;
    }
    return max;
}

void calcScore(double &score1, double &score2, double &score3, double &score4, double &score5)
{
    double min, max, avg ;
    min = findLowest(score1, score2, score3, score4, score5);    //function call to find minimum
    max = findHighest(score1, score2, score3, score4, score5);   //function call to find maximum
    double total = score1 + score2 + score3 + score4 + score5;

    total = total -( min + max );         // Subtract the min and max from the total of all 5 scores

    avg = (total / 3.0);             // Divide by 3 to take average 
    cout << "Average Score of the Contestant is: " << avg << endl;   // Display the average

}




int main()
{
    double score1, score2, score3, score4, score5;

    cout << "----------------------Welcome to Our Auditions----------------------" << endl << endl;
    // Get the Scores
    getJudgeData(score1, score2, score3, score4, score5);

    // Calculate and display the contestant's Average score
    calcScore(score1, score2, score3, score4, score5);

    return 0;

}