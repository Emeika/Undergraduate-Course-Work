#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("studentData.txt"); // open file for reading
    if (fin.fail())                  // error checking
    {
        cout << "File not found" << endl;
        return 0;
    }
    string fname, lname, topperFname, topperLname;
    int mark1, mark2, mark3, total, max = 0;
    int topperMark1 = 0; // variables for the top student record
    int topperMark2 = 0;
    int topperMark3 = 0;

    char grade;
    while (fin >> fname >> lname >> mark1 >> mark2 >> mark3) // read file until the end of file
    {
        total = mark1 + mark2 + mark3; // sum the marks of each student
        if (max < total)               // find the maximum total marks from all the students
        {
            max = total;
            topperMark1 = mark1; // store the marks for the student with the highest total mark
            topperMark2 = mark2;
            topperMark3 = mark3;
            topperFname = fname;
            topperLname = lname;

            if (max >= 90) // check the grade of the student with the highest total mark
                grade = 'A';
            else if (max >= 75)
                grade = 'B';
            else if (max >= 65)
                grade = 'C';
            else if (max >= 50)
                grade = 'D';
            else
                grade = 'F';
        }
    }
    // output the student attributes of the top student
    cout << topperFname << " " << topperLname << " " << topperMark1 << " " << topperMark2 << " " << topperMark3 << " " << max << " " << grade << endl;

    fin.close(); // close file
}