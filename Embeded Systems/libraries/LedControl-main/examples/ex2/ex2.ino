#include <LedControl.h>

// Define LED pins
LedControl ledControl(2, 3, 4, 5);

void setup() {
    Serial.begin(9600); // Start serial communication for debugging
    Serial.println("Initializing LED Control...");
    
    ledControl.begin();
    Serial.println("LED Control Initialized.");
}

void blinkNumber(int times) {
    // Blink the LEDs on and off a specified number of times
    for (int i = 0; i < times; i++) {
        ledControl.allOn();  // Turn on all LEDs to indicate blinking
        delay(500);
        ledControl.allOff(); // Turn off all LEDs
        delay(500);
    }
}

void displayBinary(int num) {
    // Display binary representation of a number on the console
    Serial.print("Displaying number: ");
    Serial.print(num);
    Serial.print(" (Binary: ");
    for (int i = 3; i >= 0; i--) {
        Serial.print((num >> i) & 1);
    }
    Serial.println(")");
}

void loop() {
    int number = 8;          // Initial number to blink and shift
    int shift_amount = 3;    // Number of shifts to the right

    // Step 1: Blink the LEDs to indicate the start of displaying the number
    Serial.println("Blinking initial number...");
    blinkNumber(3); // Blink the LEDs 3 times

    // Display initial number on the console
    displayBinary(number);

    // Step 2: Shift the number to the right and display each shift
    Serial.println("Shifting the number to the right...");

    ledControl.shiftRight(number, shift_amount); // Shift right by the specified amount

    // Update the displayed number and show it on the console after each shift
    for (int i = 0; i < shift_amount; i++) {
        number >>= 1; // Update the number by shifting it right by 1
        displayBinary(number);
        delay(1000); // Delay to observe each shift
    }

    Serial.println("End of sequence. Restarting loop...");
    delay(3000); // Delay before restarting the loop
}
