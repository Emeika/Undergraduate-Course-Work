#include <iostream>
#include "media.h"
#include "media.cpp"

using namespace std;

int main()
{
    Media m("Origin", "Dan Brown"); // object create and pass parameters to the constructor
    m.display();                    // display function called of base class
    cout << endl;

    Audio a("Haunted Bridge", "Nancy Drew", 334.4);
    a.display(); // display function called of base class and derived classes
    cout << endl;

    Video v("Sandman", "Neil Gaiman", 44);
    v.display(); // function overrides display function
    cout << endl;

    Text t("Perfume", "Patrick", 94455);
    t.display();
    cout << endl;
}