/* @file HelloKeypad.pde
|| @version 1.0
|| @author Alexander Brevig
|| @contact alexanderbrevig@gmail.com
||# GET 6 DIGIT NUMBER FROM KEYPAD 9304  GETS ITS HASH AND STORE. NEXT USER ENTERS 9304
|| @description
|| | Demonstrates the simplest use of the matrix Keypad library.
|| #
*/ 
#include <Keypad.h>
#define ON HIGH
#define OFF LOW

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
int pin = 13;

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
}
  
void loop(){
  char key = keypad.getKey();
  
  if (key){
    Serial.println(key);
    digitalWrite(pin, ON);
    delay(1000);
    digitalWrite(pin, OFF);
    
  }
  
  
}
