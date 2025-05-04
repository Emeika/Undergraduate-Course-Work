# LedControl Library for Arduino

The **LedControl** library provides a simple way to control a 4-LED setup on an Arduino. This library allows you to perform basic LED operations such as turning all LEDs on or off, counting up and down in binary, generating random numbers, and shifting bits left or right.

## Features

- Initialize the 4-LED system
- Generate random binary numbers
- Count up and down in binary (0-15)
- Shift bits left or right with specified amounts
- Turn all LEDs on or off

## Installation

1. Download the repository as a ZIP file from GitHub.
2. Extract the ZIP file and place the `LedControl` folder in your Arduino libraries directory (`Documents/Arduino/libraries`).
3. Restart the Arduino IDE if it was open during installation.

## Usage

### Including the Library

To use the library in your sketch, include the `LedControl.h` file:

```cpp
#include <LedControl.h>
```
### Initialization
```cpp
LedControl ledControl(2, 3, 4, 5); // Replace 2, 3, 4, 5 with your actual LED pins
```

### Functions
begin()
```cpp
void setup() {
    ledControl.begin();
}
```

generateRandNumber()
```cpp
ledControl.generateRandNumber();
```

upCount()
```cpp
ledControl.upCount();
```

downCount()
```cpp
ledControl.downCount();
```

shiftRight(int num, int shift_amount)
<br/>Shifts a number to the right by a specified amount and displays each shift step on the LEDs.
  - num: The initial number to display (1 to 15).
  - shift_amount: Number of times to shift the number right (1 to 4).
```cpp
ledControl.shiftRight(8, 3); // Shifts 8 to the right by 3 positions
```


shiftLeft(int num, int shift_amount)

<br/>Shifts a number to the left by a specified amount and displays each shift step on the LEDs.
  - num: The initial number to display (1 to 15).
  - shift_amount: Number of times to shift the number left (1 to 4).
```cpp
ledControl.shiftLeft(1, 2); // Shifts 1 to the left by 2 positions
```

allOff()
```cpp
ledControl.allOff();
```

allOn()
```cpp
ledControl.allOn();
```

### Example Code
```ino
#include <LedControl.h>

LedControl ledControl(2, 3, 4, 5);

void setup() {
    Serial.begin(9600);
    ledControl.begin();

    Serial.println("Random number:");
    ledControl.generateRandNumber();
    delay(2000);

    Serial.println("Counting up:");
    ledControl.upCount();
    delay(2000);

    Serial.println("Counting down:");
    ledControl.downCount();
    delay(2000);

    Serial.println("Shifting right:");
    ledControl.shiftRight(8, 3);
    delay(2000);

    Serial.println("Shifting left:");
    ledControl.shiftLeft(1, 2);
    delay(2000);

    Serial.println("Turning all LEDs on:");
    ledControl.allOn();
    delay(2000);

    Serial.println("Turning all LEDs off:");
    ledControl.allOff();
}

void loop() {
    // Empty loop
}
```
