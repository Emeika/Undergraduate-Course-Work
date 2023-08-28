#include <iostream>
#include <fstream>

using namespace std;

class Student
{
private: // not accessible outside the class
    string fname, lname, department;
    int rollNumber;
    double gpa;

public: // accessible outside the class
    // getters
    string getFname()
    {
        return fname;
    }

    string getLname()
    {
        return lname;
    }

    string getDepartment()
    {
        return department;
    }

    int getRollNumber()
    {
        return rollNumber;
    }

    double getGPA()
    {
        return gpa;
    }

    // setters
    void setFname(string fname)
    {
        this->fname = fname;
    }

    void setLname(string lname)
    {
        this->lname = lname;
    }

    void setDepartment(string department)
    {
        this->department = department;
    }

    void setRollNumber(int rollNumber)
    {
        this->rollNumber = rollNumber;
    }

    void setGPA(double gpa)
    {
        this->gpa = gpa;
    }

    // member function to calculate Grade
    char calculateGrade() const
    {
        if (gpa >= 3.6)
            return 'A';
        else if (gpa >= 3.3)
            return 'A';
        else if (gpa >= 3.0)
            return 'B';
        else if (gpa >= 2.7)
            return 'B';
        else if (gpa >= 2.3)
            return 'C';
        else if (gpa >= 2.0)
            return 'C';
        else
            return 'F';
    }
};

int main()
{
    const int maxStudent = 10;    // high maximum number of students in the file
    Student students[maxStudent]; // list of students
    int studentCount = 0;         // number of students
    string fname, lname, department;
    int rollNumber;
    double gpa;
    double gpaTotal = 0; // to calculate the gpa average

    ifstream fin("task3data.txt"); // open file for reading
    if (fin.fail())                // if file not found then error
    {
        cout << "File not found" << endl;
        return 0;
    }

    while (fin >> fname >> lname >> rollNumber >> department >> gpa) // Read every word of the file until end of file
    {
        Student s;
        s.setFname(fname); // set the object instance student name with the name in the file
        s.setLname(lname);
        s.setDepartment(department);
        s.setRollNumber(rollNumber);
        s.setGPA(gpa);
        students[studentCount] = s; // Store the student object in the array
        studentCount++;             // Increment the student count
        gpaTotal += gpa;            // Sum the GPAs for average calculation
    }

    fin.close(); // Close the file stream objects

    double average = (gpaTotal / studentCount); // Calculate the average GPA of all students

    // Print the details of all students whose GPA is greater than a certain amount
    double threshold = 0;
    cout << "Enter GPA threshold: ";
    cin >> threshold;

    cout << "Students with GPA greater than " << threshold << ":" << endl;
    for (int i = 0; i < studentCount; i++)
    {
        if (students[i].getGPA() > threshold)
        {
            cout << "First Name: " << students[i].getFname() << endl;
            cout << "Last Name: " << students[i].getLname() << endl;
            cout << "Roll Number: " << students[i].getRollNumber() << endl;
            cout << "Department: " << students[i].getDepartment() << endl;
            cout << "GPA: " << students[i].getGPA() << endl;
            cout << endl;
        }
    }

    cout << "Average GPA of all students: " << average << endl;

    // Write the details of all students with grades to a new text file called "output.txt
    ofstream fout("output.txt"); // create a new file
    if (fout.fail())
    {
        cout << "Failed to create the output file" << endl;
        return 0;
    }

    for (int i = 0; i < studentCount; i++) // loop through students in the array list
    {
        fout << "First Name: " << students[i].getFname() << endl;
        fout << "Last Name: " << students[i].getLname() << endl;
        fout << "Roll Number: " << students[i].getRollNumber() << endl;
        fout << "Department: " << students[i].getDepartment() << endl;
        fout << "GPA: " << students[i].getGPA() << endl;
        fout << "Grade: " << students[i].calculateGrade() << endl;
        fout << endl;
    }

    fout.close(); // close file
}