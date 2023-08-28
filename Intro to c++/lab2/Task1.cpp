#include <iostream>
using namespace std;

int main()

{ 
    //Task 1  
    char inp;
    cout << "Enter Character: ";
    cin >> inp;
    
    if ((inp < 'A') || (inp > 'Z' && inp < 'a') || (inp > 'z')) {
        cout << "Invalid Character";
    }
        
    else {
    
    
        switch(inp) {
            case 'A':
                cout << "Vowel" << "\n";
                break;
            case 'E':
                cout << "Vowel" << "\n";
                break;
            case 'I':
                cout << "Vowel" << "\n";
                break;
                
            case 'O':
                cout << "Vowel" << "\n";
                break;
            case 'U':
                cout << "Vowel" << "\n";
                break;
            case 'a':
                cout << "Vowel" << "\n";
                break;
            case 'e':
                cout << "Vowel" << "\n";
                break;
            case 'i':
                cout << "Vowel" << "\n";
                break;
            case 'o':
                cout << "Vowel" << "\n";
                break;
            case 'u':
                cout << "Vowel" << "\n";
                break;
            default:
                cout << "Consonant" << "\n";
                
        }
    }
    

    return 0;
}
