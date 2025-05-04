#include <Keypad.h>

// Define the number of digits and pins for the display
const int dataPin = 2;    // DS (Data Pin)
const int latchPin = 4;   // ST_CP (Latch Pin)
const int clockPin = 3;   // SH_CP (Clock Pin)

// Define pins for controlling individual digits
const int DIGIT_1_PIN = 5;
const int DIGIT_2_PIN = 6;
const int DIGIT_3_PIN = 7;
const int DIGIT_4_PIN = 8;

// Define 7-segment digit patterns for numbers 0-9 (A-G, DP) for common anode displays
byte digitCode[] = {
  0xC0, // 0
  0xF9, // 1
  0xA4, // 2
  0xB0, // 3
  0x99, // 4
  0x92, // 5
  0x82, // 6
  0xF8, // 7
  0x80, // 8
  0x90  // 9
};

// Define custom patterns for letters 'F', 'C', 'U'
byte FCCU[] = {
  0x8E, // F
  0xC6, // C
  0xC1 // U
};

// Keypad settings
const byte ROWS = 4; 
const byte COLS = 4; 
char keys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {9, 10, 11, 12}; // Rows connected to Arduino pins 9-12
byte colPins[COLS] = {A0, A1, A2, A3}; // Columns connected to analog pins A0-A3

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

int minutes = 0, seconds = 0; // Default values for the stopwatch
bool editingMinutes = false;
bool editingSeconds = false;
bool running = false;
bool countingUp = false; // True if counting upwards

unsigned long lastMillis = 0;  // Timer for countdown or count-up

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);

  // Set digit pins as outputs
  pinMode(DIGIT_1_PIN, OUTPUT);
  pinMode(DIGIT_2_PIN, OUTPUT);
  pinMode(DIGIT_3_PIN, OUTPUT);
  pinMode(DIGIT_4_PIN, OUTPUT);

  Serial.begin(9600); // Start Serial Monitor for debugging
  Serial.println("Stopwatch initialized. Ready to accept inputs.");
}

void loop() {
  char key = keypad.getKey();
  
  if (key) {
    Serial.print("Key pressed: ");
    Serial.println(key);  // Output keypress for debugging

    // Handle keypad input
    switch (key) {
      case 'A': // Edit seconds
        editingSeconds = true;
        editingMinutes = false;
        Serial.println("Editing seconds.");
        break;
      case 'B': // Edit minutes
        editingMinutes = true;
        editingSeconds = false;
        Serial.println("Editing minutes.");
        break;
      case 'C': // Start/Stop stopwatch or start count-up if time is 00:00
        if (!running) {
          if (minutes == 0 && seconds == 0) {
            countingUp = true;  // If time is 00:00, start counting upwards
            Serial.println("Count-up started.");
          } else {
            countingUp = false; // Regular countdown
            Serial.println("Countdown started.");
          }
          running = true;
          lastMillis = millis();
        } else {
          running = false; // Pause if already running
          Serial.println("Stopwatch paused.");
        }
        break;
      case 'D': // Reset the stopwatch
        resetStopwatch();
        break;
      default:
        // Modify seconds (0-59) and minutes (0-99)
        if (editingSeconds && key >= '0' && key <= '9') {
          int value = key - '0';  // Convert char to int
          seconds = (seconds * 10 + value) % 60; // Limit to 0-59
          Serial.print("Seconds set to: ");
          Serial.println(seconds);
          editingSeconds = false;
        }
        if (editingMinutes && key >= '0' && key <= '9') {
          int value = key - '0';  // Convert char to int
          minutes = (minutes * 10 + value) % 100; // Limit to 0-99
          Serial.print("Minutes set to: ");
          Serial.println(minutes);
          editingMinutes = false;
        }
        break;
    }
  }

  // Stopwatch logic (either counting down or counting up)
  if (running && millis() - lastMillis >= 1000) {
    lastMillis = millis();
    
    if (countingUp) {
      // Count up logic
      seconds++;
      if (seconds > 59) {
        seconds = 0;
        minutes++;
      }
    } else {
      // Countdown logic
      seconds--;
      if (seconds < 0) {
        seconds = 59;
        if (minutes > 0) {
          minutes--;
        } else {
          // Time's up, blink "FCCU" and reset
          Serial.println("Time's up! Blinking FCCU...");
          displayFCCU();  // Call FCCU display
          resetStopwatch();
        }
      }
    }

    Serial.print("Time: ");
    Serial.print(minutes);
    Serial.print(":");
    Serial.println(seconds);
  }

  // Continuously display time by multiplexing digits
  displayTime();
}

// Function to multiplex the digits and display the current time
void displayTime() {
  // Show ones place of seconds (Digit 1)
  digitalWrite(DIGIT_1_PIN, HIGH);      // Enable digit 1 (Right-most)
  showDigit(digitCode[seconds % 10]);   // Show ones of seconds
  delay(5);                             // Small delay to allow digit to be visible
  digitalWrite(DIGIT_1_PIN, LOW);       // Disable digit 1

  // Show tens place of seconds (Digit 2)
  digitalWrite(DIGIT_2_PIN, HIGH);      // Enable digit 2
  showDigit(digitCode[seconds / 10]);   // Show tens of seconds
  delay(5);                             // Small delay to allow digit to be visible
  digitalWrite(DIGIT_2_PIN, LOW);       // Disable digit 2

  // Show ones place of minutes (Digit 3)
  digitalWrite(DIGIT_3_PIN, HIGH);      // Enable digit 3
  showDigit(digitCode[minutes % 10]);   // Show ones of minutes
  delay(5);                             // Small delay to allow digit to be visible
  digitalWrite(DIGIT_3_PIN, LOW);       // Disable digit 3

  // Show tens place of minutes (Digit 4)
  digitalWrite(DIGIT_4_PIN, HIGH);      // Enable digit 4 (Left-most)
  showDigit(digitCode[minutes / 10]);   // Show tens of minutes
  delay(5);                             // Small delay to allow digit to be visible
  digitalWrite(DIGIT_4_PIN, LOW);       // Disable digit 4
}

// Helper function to send the digit code to the shift register
void showDigit(byte digitValue) {
  digitalWrite(latchPin, LOW);           // Prepare shift register
  shiftOut(dataPin, clockPin, MSBFIRST, digitValue); // Send digit pattern
  digitalWrite(latchPin, HIGH);          // Apply the value to the display
}

void displayFCCU() {
  for (int blinkCount = 0; blinkCount < 4; blinkCount++) {  // Blink 4 times
    // Display "FCCU" for 500ms
    for (int i = 0; i < 15; i++) {  // Refresh display for 500ms (5ms * 100 = 500ms)
      // Display F
      showDigit(FCCU[0]);
      digitalWrite(DIGIT_4_PIN, HIGH);
      delay(5);
      digitalWrite(DIGIT_4_PIN, LOW);

      // Display C (first C)
      showDigit(FCCU[1]);
      digitalWrite(DIGIT_3_PIN, HIGH);
      delay(5);
      digitalWrite(DIGIT_3_PIN, LOW);

      // Display C (second C)
      showDigit(FCCU[1]);
      digitalWrite(DIGIT_2_PIN, HIGH);
      delay(5);
      digitalWrite(DIGIT_2_PIN, LOW);

      // Display U
      showDigit(FCCU[2]);
      digitalWrite(DIGIT_1_PIN, HIGH);
      delay(5);
      digitalWrite(DIGIT_1_PIN, LOW);
    }

    // Turn off the display (clear) for 500ms
    clearDisplay();
    delay(500);
  }
}



// Function to reset the stopwatch after the countdown or count-up
void resetStopwatch() {
  minutes = 0;
  seconds = 0;
  running = false;
  countingUp = false;
  Serial.println("Stopwatch reset to 00:00.");
  displayTime();
}

// Function to clear the display
void clearDisplay() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(latchPin, LOW);
    shiftOut(dataPin, clockPin, MSBFIRST, 0xFF); // Clear digit (turn off segments)
    digitalWrite(latchPin, HIGH);
    delay(5);
  }
}
