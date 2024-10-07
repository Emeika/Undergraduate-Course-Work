#include <Key.h>
#include <Keypad.h>

#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};

byte rowPins[ROWS] = {6, 7, 8, 9};
byte colPins[COLS] = {10, 11, 12};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

int LED = 2;

String inputAmount = "";
int fuelAmount = 0;

void setup() {
  Serial.begin(9600);

  pinMode(LED, OUTPUT);

  for (int i = 0; i < 3; i++) {
    digitalWrite(LED, HIGH);
    delay(500);
    digitalWrite(LED, LOW);
    delay(500);
  }
  
  Serial.println("Enter amount:");
}

void loop() {
  char key = keypad.getKey();
  
  if (key) {
    if (key >= '0' && key <= '9') {
      inputAmount += key;
      
      Serial.print(key); 
      
    } else if (key == '#') {
      
      fuelAmount = inputAmount.toInt();
      
      if (fuelAmount > 0 && fuelAmount < 9999) {
        
        Serial.println();
        Serial.sprint("You entered: ");
        Serial.println(fuelAmount);
        
        int liters = fuelAmount / 200;
        
        if (liters >= 1) {
          Serial.print("You will have ");
          Serial.print(liters);
          Serial.print(" of fuel against this amount.");
          Serial.println("\nDispensing fuel. Please wait");
          
          for (int i = 0; i < liters; i++) {
            delay(500);  
            digitalWrite(LED, HIGH);
            delay(1000);
            digitalWrite(LED, LOW);
            delay(1000);
          }
          
          Serial.println("Thank you for visiting us. \nDrive safe.");
          
        } else {
          Serial.println("Sorry, system cannot dispense fuel against this amount.");
          Serial.println("Thank you for visiting us. \nDrive safe.");
        }
      } else {
        Serial.println("Invalid amount entered. Please try again.");
      }
      
      inputAmount = "";
    } else if (key == '*') {
      inputAmount = "";
      Serial.println();
      Serial.println("Input cleared.");
    }
  }
}
