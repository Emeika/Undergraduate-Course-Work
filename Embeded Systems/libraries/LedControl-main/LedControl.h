#ifndef LedControl_h
#define LedControl_h

#include <Arduino.h>

class LedControl
{
private:
    int ledPins[4];

public:
    LedControl(int pin1, int pin2, int pin3, int pin4);
    void begin();
    void generateRandNumber();
    void upCount();
    void downCount();
    void shiftRight(int num, int shift_amount);
    void shiftLeft(int num, int shift_amount);
    void allOff();
    void allOn();
};
#endif
