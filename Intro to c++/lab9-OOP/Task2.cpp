#include <iostream>
#include <fstream>
using namespace std;

struct Vehicle
{
    string make;
    double hp;
};

void mostPowerful(const Vehicle *vehicles, int size, const string &make)
{
    double maxPower = 0.0;
    cout << vehicles[0].make << endl;
    for (int i = 0; i < size; i++)
    {
        // if make == Toyota then compare if its hp is greater than current hp

        if (vehicles[i].make == make && vehicles[i].hp > maxPower)
        {
            maxPower = vehicles[i].hp;
        }
    }

    if (maxPower > 0.0)
    {
        cout << "The most powerful " << make << " vehicle has " << maxPower << " horsepower." << endl;
    }
    else
    {
        cout << "No " << make << " vehicles found." << endl;
    }
}

int main()
{
    ifstream fin("VehicleInfo.txt"); // Open file
    if (fin.fail())
    {
        cout << "Error opening file ";
        return 0;
    }
    int lineCount = 0;
    string line;
    while (getline(fin, line))
    {
        lineCount++;
    }

    fin.clear();
    fin.seekg(0, ios::beg); // Reset file stream to the beginning

    Vehicle *vehicles = new Vehicle[lineCount]; // Dynamic Array of Vehicle STRUCTS

    string make;
    int year;
    double hp;
    int index = 0;

    while (fin >> make >> year >> hp)
    {
        vehicles[index] = {make, hp}; // Create Vehicle struct and assign it to the array
        index++;
    }

    string makeToFind = "Toyota";
    mostPowerful(vehicles, lineCount, makeToFind);

    delete[] vehicles; // Free the dynamically allocated memory

    return 0;
}
