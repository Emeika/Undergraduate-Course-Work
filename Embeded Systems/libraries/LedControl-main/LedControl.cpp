#include "LedControl.h"

// Constructor to initialize LED pins
LedControl::LedControl(int pin1, int pin2, int pin3, int pin4)
{
    ledPins[0] = pin1;
    ledPins[1] = pin2;
    ledPins[2] = pin3;
    ledPins[3] = pin4;
}

// Initialize the LED pins as outputs
void LedControl::begin()
{
    for (int i = 0; i < 4; i++)
    {
        pinMode(ledPins[i], OUTPUT);
    }
}

// Generate a random number between 0 and 15 and display it in binary
void LedControl::generateRandNumber()
{
    int randNum = random(0, 16); // Generates a number from 0 to 15
    for (int i = 0; i < 4; i++)
    {
        digitalWrite(ledPins[i], (randNum >> i) & 1);
    }
}

// Count up from 0 to 15 with a 2-3 second delay in binary
void LedControl::upCount()
{
    for (int i = 0; i <= 15; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            digitalWrite(ledPins[j], (i >> j) & 1);
        }
        delay(2000); // 2-second delay between counts
    }
}

// Count down from 15 to 0 in binary
void LedControl::downCount()
{
    for (int i = 15; i >= 0; i--)
    {
        for (int j = 0; j < 4; j++)
        {
            digitalWrite(ledPins[j], (i >> j) & 1);
        }
        delay(2000); // 2-second delay between counts
    }
}

// Shift right operation for binary representation
void LedControl::shiftRight(int num, int shift_amount)
{
    if (num < 1 || num > 15 || shift_amount < 1 || shift_amount > 4)
        return;

    for (int i = 0; i < 4; i++)
    {
        digitalWrite(ledPins[i], (num >> i) & 1);
    }
    delay(2000); // Pause to display initial number

    for (int i = 0; i < shift_amount; i++)
    {
        num >>= 1; // Shift right by 1
        for (int j = 0; j < 4; j++)
        {
            digitalWrite(ledPins[j], (num >> j) & 1);
        }
        delay(1000); // 1-second delay for each shift
    }
}

// Shift left operation for binary representation
void LedControl::shiftLeft(int num, int shift_amount)
{
    if (num < 1 || num > 15 || shift_amount < 1 || shift_amount > 4)
        return;

    for (int i = 0; i < 4; i++)
    {
        digitalWrite(ledPins[i], (num >> i) & 1);
    }
    delay(2000); // Pause to display initial number

    for (int i = 0; i < shift_amount; i++)
    {
        num <<= 1; // Shift left by 1
        for (int j = 0; j < 4; j++)
        {
            digitalWrite(ledPins[j], (num >> j) & 1);
        }
        delay(1000); // 1-second delay for each shift
    }
}

// Turn off all LEDs
void LedControl::allOff()
{
    for (int i = 0; i < 4; i++)
    {
        digitalWrite(ledPins[i], LOW);
    }
}

// Turn on all LEDs
void LedControl::allOn()
{
    for (int i = 0; i < 4; i++)
    {
        digitalWrite(ledPins[i], HIGH);
    }
}
