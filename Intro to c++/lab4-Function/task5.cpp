#include <iostream>
#include <string>
using namespace std;

const int NUM_STUDENTS = 10;
const int NUM_TESTS = 5;

// Function to read and store data into two arrays
void read_data(string names[], int scores[][NUM_TESTS]) {
    for (int i = 0; i < NUM_STUDENTS; i++) {
        // Prompt user to enter name of student
        cout << "Enter name or \"-1\" to stop: ";
        getline(cin, names[i]);    // Take the string name with spaces as a single name

        if (names[i] == "-1") {    // take no more names if user enters -1 = print the entered data
            break;
        }

        // Prompt user to enter marks for each test
        for (int j = 0; j < NUM_TESTS; j++) {
            int score;
            do {
                cout << "Enter " << names[i] << "'s marks for test " << j+1 << ": ";
                cin >> score;
            } while (score < 0 || score > 100);    // Check to accept score between 0 and 100 inclusive
            scores[i][j] = score;   // score stored against every student in 2d
        }
        cin.ignore(); // Ignore newline character
    }
}

// Function to calculate average test score and grade
char calculate_grade(float avg_score) {
    // criteria set using if else to return the relevant grade depending on the average score for each student
    if (avg_score >= 90) {
        return 'A';
    } else if (avg_score >= 80) {
        return 'B';
    } else if (avg_score >= 70) {
        return 'C';
    } else if (avg_score >= 60) {
        return 'D';
    } else {
        return 'F';
    }
}

// Function to output results
void output_results(string names[], int scores[][NUM_TESTS], char grades[]) {
    cout << "Names\t\t\t\t Marks\t\t\t Average\t\t Grades" << endl;

    for (int i = 0; i < NUM_STUDENTS; i++) {
        if (names[i] == "-1") {
            break;   // if no data has been entered then nothing to display
        }

        // Output student name and marks for each test
        cout << names[i] << "\t\t\t";
        for (int j = 0; j < NUM_TESTS; j++) {
            cout << scores[i][j] << " ";
        }

        // Calculate average test score
        float avg_score = 0;
        for (int j = 0; j < NUM_TESTS; j++) {    // loop to calculate the average from within the array
            avg_score += scores[i][j];       // the total of all scores in the 2d list for a student
        }
        avg_score /= NUM_TESTS;      // average = total / no. of entries

        // Calculate grade based on average test score
        char grade = calculate_grade(avg_score);   // function call to get grade
        grades[i] = grade;    // grade stored in the array

        // Output average test score and grade
        cout << "\t\t\t" << avg_score << "\t\t\t" << grade << endl;
    }

    // Calculate and output class average
    float class_avg = 0;
    int num_students = 0;
    for (int i = 0; i < NUM_STUDENTS; i++) {
        if (names[i] == "-1") {
            break;
        }

        // Calculate average test score for each student and add to class average
        float student_avg = 0;
        for (int j = 0; j < NUM_TESTS; j++) {
            student_avg += scores[i][j];
        }
        student_avg /= NUM_TESTS;
        class_avg += student_avg;

        num_students++;
    }
    class_avg /= num_students;
    cout << endl << "Class average is: " << class_avg << endl;
}

int main() {
    // declaring the arrays
    string names[NUM_STUDENTS];
    int scores[NUM_STUDENTS][NUM_TESTS];  //2d array for scores
    char grades[NUM_STUDENTS] = {0};

    cout << "Enter names and marks of students:-" << endl;
    cout << "#Enter \'-1\' to end the entries." << endl;

    read_data(names, scores);
    output_results(names, scores, grades);

    return 0;
}
