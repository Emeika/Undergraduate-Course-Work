/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

class Point
{
// Declare member variables
private:
  double x, y;

// Define member functions
public:
  // Default constructor
  Point()
  {
    x = 0.0;
    y = 0.0;
  }
  
  // Constructor with parameters
  Point(double newX, double newY)
  {
    x = newX;
    y = newY;
  }

  // Calculate distance from origin
  double distance() const
  {
    return sqrt(x * x + y * y);
  }

  // Print point in (x, y) format
  void print() const
  {
    cout << "(" << x << ", " << y << ")";
  }
};

// Find the point with the greatest distance from the origin
Point getFurthestPoint(const Point *arr, int size)
{
  Point furthestPoint;
  double maxDistance = 0.0;
  for (int i = 0; i < size; i++)
  {
    double distance = arr[i].distance();
    if (distance > maxDistance)
    {
      maxDistance = distance;
      furthestPoint = arr[i];
    }
  }
  return furthestPoint;
}

int main()
{
  int size;
  cout << "Enter array size: ";
  cin >> size;

  // Allocate memory for dynamic array of points
  Point *pointarray = new Point[size];

  // Seed the random number generator with the current time
  srand(time(0));

  // Initialize the array with random points
  for (int i = 0; i < size; i++)
  {
    double x = rand() % 9 - 3; // Generate a random integer in the range [0, 8], then shift it down by 3    
    double y = rand() % 9 - 3;
    pointarray[i] = Point(x, y);
  }

  // Print each point and its distance from the origin
  for (int i = 0; i < size; i++)
  {
    cout << "Point: " << i << ": ";
    pointarray[i].print();
    cout << " Distance: " << pointarray[i].distance() << endl;
  }

  // Find the furthest point and print it
  Point furthestPoint = getFurthestPoint(pointarray, size);
  cout << "Furthest point: ";
  furthestPoint.print();
  cout << " Distance: " << furthestPoint.distance() << endl;

  // Deallocate memory for dynamic array of points
  delete[] pointarray;
  
  
  
}

