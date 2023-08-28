#include <iostream>
#include <fstream>
using namespace std;

class Vehicle
{
private: // private member variables
    string make;
    int year;
    double hp; // horse power of the vehicle

public: // public methods
    // Default constructor
    Vehicle()
    {
        make = "";
        year = 0;
        hp = 0;
    }

    // Constructor
    Vehicle(string make, int year, double hp)
    {
        this->make = make;
        this->year = year;
        this->hp = hp;
    }

    // Getters
    string getMake()
    {
        return this->make;
    }

    int getYear()
    {
        return this->year;
    }

    double getHP()
    {
        return this->hp;
    }
};

Vehicle *readVehicleInventory(string file) // Functions returns array of vehicle objects
{

    ifstream fin(file); // Open file
    if (fin.fail())     // if we can't open the file then return NULL instead
    {
        cout << "Error opening file ";
        return nullptr;
    }
    int lineCount = 0; // Number of lines to find the size of file for the array
    string line;
    while (getline(fin, line))
    {
        lineCount++;
    }

    fin.clear();
    fin.seekg(0, ios::beg); // Reset file stream to the beginning

    Vehicle *vehicle = new Vehicle[lineCount]; // Dynamic Array of Vehicle objects

    string make;
    int year;
    double hp;
    int index = 0;

    while (fin >> make >> year >> hp) // Read each word in the file and increment the index
    {
        vehicle[index] = Vehicle(make, year, hp); // Create Vehicle object and assign it to the array

        index++;
    }

    for (int i = 0; i < lineCount; i++) // print
    {
        cout << "Vehicle " << (i + 1) << ":" << endl;
        cout << "Make: " << vehicle[i].getMake() << endl;
        cout << "Year: " << vehicle[i].getYear() << endl;
        cout << "Horsepower: " << vehicle[i].getHP() << endl;
        cout << endl;
    }

    fin.close(); // Close the file

    return vehicle; // Return the array of Vehicle objects
}

int main()
{

    Vehicle *arr = readVehicleInventory("VehicleInfo.txt"); // Read vehicle inventory from file
    delete[] arr;                                           // Deallocate memory for the array of Vehicle objects
}