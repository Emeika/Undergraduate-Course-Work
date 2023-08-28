#include <iostream>
#include <string> 
using namespace std; 

struct StudentRecord { //Definition of structure "StudentRecord" which contains student's data.
    string name;
    float test;
    float midterm;
    float final;
    char letterGrade;
};

char computeLetterGrade(float average) {
    //Function returns a character for letter grade corresponding to the average.
    if (average < 50) { 
        return 'F';
    } else if (average < 60) {
        return 'D';
    } else if (average < 75) {
        return 'C';
    } else if (average < 90) {
        return 'B';
    } else {
        return 'A';
    }
}

void viewRecord(const StudentRecord& record) { //Function which accepts a structure 
    //variable of type "StudentRecord" const reference and prints student's data.
    cout << "Name: " << record.name << "\n";
    cout << "Test score: " << record.test << "\n";
    cout << "Midterm score: " << record.midterm << "\n";
    cout << "Final score: " << record.final << "\n";
    cout << "Letter grade: " << record.letterGrade << "\n\n";
}

int main() {
    StudentRecord record; //Instantiating an object of structure "StudentRecord".
    cout << "Enter student name: ";
    getline(cin, record.name); //Reading input for student's name using "getline" method.
    cout << "Enter test score: ";
    cin >> record.test; 
    cout << "Enter midterm score: ";
    cin >> record.midterm; 
    cout << "Enter final score: ";
    cin >> record.final; 

    //Computing the weighted average of student's three test scores.
    float average = record.test * 0.2 + record.midterm * 0.3 + record.final * 0.5; 

    //Storing the letter grade corresponding to the computed average in the structure.
    record.letterGrade = computeLetterGrade(average); 

    viewRecord(record); //Printing student's data

}
