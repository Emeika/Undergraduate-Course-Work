#include <iostream>
#include <string>

using namespace std;

class Course {
// Member variables
private:
    string name;
    float test;
    float midterm;
    float final;
    char letterGrade;
    
// Member functions
public:
    // Default constructor
    Course() {
        name = "";
        test = 0.0;
        midterm = 0.0;
        final = 0.0;
        letterGrade = 'F';
    }

    // Non-default constructor with only name argument
    Course(string n) {
        name = n;
        test = 0.0;
        midterm = 0.0;
        final = 0.0;
        letterGrade = 'F';
    }

    // Non-default constructor with name and assessments arguments
    Course(string n, float t, float m, float f) {
        name = n;
        test = t;
        midterm = m;
        final = f;
        calculateLetterGrade();
    }

    // Getters
    string getName() {
        return name; 
        
    }
    float getTest(){
        return test; 
        
    }
    float getMidterm() {
        return midterm; 
        
    }
    float getFinal()  {
        return final; 
        
    }
    char getLetterGrade() {
        return letterGrade; 
        
    }

    // Setters
    void setName(string n) { 
        name = n; 
        
    }
    void setTest(float t) {
        test = t; calculateLetterGrade(); 
        
    }
    void setMidterm(float m) {
        midterm = m; calculateLetterGrade(); 
        
    }
    
    void setFinal(float f) { 
        final = f; calculateLetterGrade(); 
        
    }

    // Print member function
    void print() const {
        cout << "Name: " << name << endl;
        cout << "Test score: " << test << endl;
        cout << "Midterm score: " << midterm << endl;
        cout << "Final score: " << final << endl;
        cout << "Letter grade: " << letterGrade << endl;
        cout << "\n\n";
    }

private:
    // Helper function to calculate the letter grade
    void calculateLetterGrade() {
        float total = test + midterm + final;
        if (total >= 90) {
            letterGrade = 'A';
        } else if (total >= 75) {
            letterGrade = 'B';
        } else if (total >= 60) {
            letterGrade = 'C';
        } else if (total >= 50) {
            letterGrade = 'D';
        } else {
            letterGrade = 'F';
        }
    }
};

int main() {
    // Create a default course
    Course defaultCourse;
    defaultCourse.print();
    

    // Create a course with name only
    Course nameOnlyCourse("Hafsah Shahbaz");
    nameOnlyCourse.print();

    // Create a course with all assessments
    Course allAssessmentsCourse("Ahmad", 15.0, 20.0, 35.0);
    allAssessmentsCourse.print();

    // Modify the assessments of the course with all assessments and print again
    allAssessmentsCourse.setTest(18.0);
    allAssessmentsCourse.setMidterm(25.0);
    allAssessmentsCourse.setFinal(42.0);
    allAssessmentsCourse.print();

    return 0;
}



