#include <iostream>
#include <string>
using namespace std;

struct Drink {  // Define a struct to represent a drink
    // Member variables:
    string name;
    double cost;
    int quantity;
};

void displayMenu(const Drink* drinks, int size) {  // Display the drink menu
    cout << "-----------------------------------------------------\n";
    cout << "                 DRINK MENU\n";
    cout << "-----------------------------------------------------\n";
    cout << "Drink Name         Cost            Number in machine\n";
    for (int i = 0; i < size; i++) {
        // Use printf to format the output for the drink details
        printf("%d. %-15s $%6.2f %10d\n", i+1, drinks[i].name.c_str(), drinks[i].cost, drinks[i].quantity);
    }
    cout << "0. Quit\n";
    cout << "-----------------------------------------------------\n\n";
}


double getValidAmount() {
    double amount;
    do {  // Loop until a valid amount is entered
        cout << "Enter amount (up to $1.00): $";
        cin >> amount;
    } while (amount < 0 || amount > 1.0);   // if negative or greater than 1 loop 
    return amount;
}

int main() {
    const int NUM_DRINKS = 4;

    // Create an array of Drink structs representing the drinks in the machine
    Drink* drinks = new Drink[NUM_DRINKS] {
        {"Cola", 0.75, 20},
        {"Root Beer", 0.75, 20},
        {"Grape Soda", 0.80, 20},
        {"Cream Soda", 0.80, 20} 
        };

    // total amount of money earned
    double totalEarned = 0.0;

    while (true) {  //Loop until the user chooses to quit
        cout << endl;
        displayMenu(drinks, NUM_DRINKS);

        int choice;
        cout << "Enter choice (0-4): ";
        cin >> choice;    // get user choice 

        if (choice == 0) {
            break; // exit loop
        } else if (choice >= 1 && choice <= NUM_DRINKS) {  //if Choice between 1 to 4
            Drink& chosenDrink = drinks[choice-1];

             // Check if the chosen drink is available
            if (chosenDrink.quantity > 0) {

                // Get the amount of money from the user
                double amount = getValidAmount();

                // Check if the user has inserted enough money
                if (amount >= chosenDrink.cost) {
                    double change = amount - chosenDrink.cost;  // Get change 
                    cout << "Dispensing " << chosenDrink.name << "\n";
                    printf("Change: $%.2f\n", change);
                    totalEarned += chosenDrink.cost;  // Add to total earned    
                    chosenDrink.quantity--;    // subtract the drink quantity by
                } else {
                    printf("Not enough money. Please insert $%.2f\n", chosenDrink.cost);
                }
            } else {
                cout << "Sorry, " << chosenDrink.name << " is sold out.\n";
            }
        } else {
            cout << "Invalid choice. Please try again.\n";
        }
    }

    printf("Total amount earned: $%.2f\n" , totalEarned);

    delete[] drinks; // free memory

}
