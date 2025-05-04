#include <LedControl.h>

// Define LED pins
LedControl ledControl(2, 3, 4, 5);

void setup() {
    Serial.begin(9600); // Start serial communication for debugging
    Serial.println("Initializing LED Control...");
    
    ledControl.begin();
    Serial.println("LED Control Initialized.");
        Serial.println("Testing allOn()...");
    ledControl.allOn();
    delay(2000);

    Serial.println("Testing allOff()...");
    ledControl.allOff();
    delay(2000);

    Serial.println("Testing generateRandNumber()...");
    ledControl.generateRandNumber();
    delay(2000);

    Serial.println("Testing upCount()...");
    ledControl.upCount();
    delay(2000);

    Serial.println("Testing downCount()...");
    ledControl.downCount();
    delay(2000);

    Serial.println("Testing shiftRight() with num=8, shift_amount=3...");
    ledControl.shiftRight(8, 3);
    delay(2000);

    Serial.println("Testing shiftLeft() with num=1, shift_amount=3...");
    ledControl.shiftLeft(1, 3);
    delay(2000);

    Serial.println("End of all tests. Restarting loop...");
}

void loop() {
}
