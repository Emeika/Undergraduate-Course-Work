/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <string>

using namespace std;

int main()

//Task 1
{
    int l, b, h, ls, tl;  // Declaring of variables
    cout << "Enter length ";
    cin >> l;
    cout << "Enter Width ";
    cin >> b;
    cout << "Enter Height: ";
    cin >> h;
    ls = 2 * h * l + b;    //Lateral Surface area
    tl = 2 *( (l*b) + (b*h) + (l*h) );  //Total surface area
    cout << ls << endl << tl << endl;  // endl moves to next line
    
    // Task2
    int x, y;
    cout << "Enter 2 numbers: ";
    cin >> x >> y;
    if (y%x == 0) {
        cout << y << " is a factor" << endl;   // If remainder is 0 then it is a factor else not
    } else {
        cout << y << " Not a factor." << endl;
    }
    

    
    // Task4
    int ctemp , ftemp;
    cout << "Enter temperature in Celsius: ";
    cin >> ctemp;
    ftemp = ((9/5) * ctemp) + 32;   // Formula coverts to F
    cout <<  "temperature in Fahrenheit : " << ftemp << "\n";
    
    //Task5
    int days, miles, cost;
    cout << "Enter the number of days and miles driven: ";
    cin >> days >> miles;
    cost = 30 * days + 0.5 * miles;
    cout << "Total cost of rental: " << cost << endl;

    
    
    
    //Task6
    int weight , height, bmi;
    cout << "Enter the user's weight(kg) and height(m) : ";  //Enter weight and height following a space
    cin >> weight >> height;
    bmi = weight/ height;
    cout << "BMI: " << bmi << endl;

    //Task 7
    int age , years, months, d;
    cout << "Enter the user's age (total number of days): ";
    cin >> age;
    years = (int)age/ 365;   // integer division as one year has 365 days
    months = (int)(age % 365) / 30;    // a month has 30 days so integer division to get 
    d = (int)(age % 365) % 30;
    cout << "years: " << years << "months: " << months << "days: " << d << endl;
    
    
}


