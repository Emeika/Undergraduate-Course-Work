#include <LiquidCrystal.h>

// Initialize the LCD (RS, E, D4-D7 pins)
LiquidCrystal lcd(12, 11, 2, 3, 4, 5);

void setup() {
  // Initialize the LCD
  lcd.begin(16, 2); // Set up the LCD as a 16x2 display
  lcd.setCursor(0, 0); // Set cursor to the first column, first row
  lcd.print("Gas Volume:"); // Print a test message on the first row

  // Initialize Serial Monitor
  Serial.begin(9600); // Start serial communication at 9600 baud rate
  Serial.println("System Initialized"); // Debug message
}

void loop() {
  // Read the potentiometer value (0 to 1023)
  int potValue = analogRead(A0);

  // Map potentiometer value to gas volume (0 to 100 cubic feet)
  int gasVolume = map(potValue, 0, 1023, 0, 100);

  // Display the mapped gas volume on the LCD
  lcd.setCursor(0, 1); // Move to the second row
  lcd.print("Volume: ");
  lcd.print(gasVolume); // Print the gas volume
  lcd.print(" c-ft  "); // Add unit

  // Print the readings to the Serial Monitor
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print(" | Mapped Gas Volume: ");
  Serial.println(gasVolume);

  delay(500); // Small delay for stability
}
