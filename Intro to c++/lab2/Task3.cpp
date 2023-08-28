/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;

int main()
{
    //Task3
    
    int num, last, zero=0, one = 0, two = 0, three=0, four=0, five=0, six=0, seven=0, eight=0, nine=0;
    cout << "Enter number: ";
    cin >> num;
    while(num>0){
        last = num% 10;
        num = num/ 10;
        
    
        switch(last) {
            case 0:
                zero += 1;
                break;
            
            case 1:
                one += 1;
                break;
            
            case 2:
                two += 1;
                break;
            
            case 3:
                three += 1;
                break;
            case 4:
                four += 1;
                break;
            case 5:
                five += 1;
                break;
            case 6:
                six += 1;
                break;
            case 7:
                seven += 1;
                break;
            case 8:
                eight += 1;
                break;
            case 9:
                nine += 1;
                break;

    }
        
    }
    cout << "The frequency of 0 = " << zero << endl;
    cout << "The frequency of 1 = " << one << endl;
    cout << "The frequency of 2 = " << two << endl;
    cout << "The frequency of 3 = " << three << endl;
    cout << "The frequency of 4 = " << four << endl;
    cout << "The frequency of 5 = " << five << endl;
    cout << "The frequency of 6 = " << six << endl;
    cout << "The frequency of 7 = " << seven << endl;
    cout << "The frequency of 8 = " << eight << endl;
    cout << "The frequency of 9 = " << nine << endl;
    
    

    

    return 0;
}