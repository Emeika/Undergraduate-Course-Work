// Define pins
int pirPin = 2;        // PIR sensor is connected to digital pin 2
int ledPin = 13;       // LED is connected to digital pin 13
int ldrPin = A0;       // LDR is connected to analog pin A0

// Variables for managing LED and motion states
bool ledOn = false;                // Tracks if the LED is currently on
unsigned long motionEndTime = 0;   // Time when motion was last detected
unsigned long ledTurnOffDelay = 10000;  // Time to keep LED on after no motion (10 seconds)
unsigned long ledMaxOnTime = 120000;    // Maximum time to keep LED on (120 seconds)

// Thresholds
int ldrThreshold = 500;            // Threshold for LDR value (adjust according to your environment)

void setup() {
  // Initialize pins
  pinMode(pirPin, INPUT);   // PIR sensor as input
  pinMode(ledPin, OUTPUT);  // LED as output
  Serial.begin(9600);       // Initialize serial communication
}

void loop() {
  int pirState = digitalRead(pirPin);  // Read the PIR sensor state
  int ldrValue = analogRead(ldrPin);   // Read the LDR value

  // Display LDR and PIR values for debugging purposes
  Serial.print("LDR Value: ");
  Serial.print(ldrValue);
  Serial.print(" | PIR State: ");
  Serial.println(pirState);

  // Condition: If it's dark (LDR value below threshold) and motion is detected
  if (ldrValue < ldrThreshold && pirState == HIGH) {
    digitalWrite(ledPin, HIGH);      // Turn on LED
    ledOn = true;                    // Set LED on flag
    motionEndTime = millis();        // Record the time motion was detected
  }

  // If motion is detected, keep updating the motionEndTime
  if (pirState == HIGH) {
    motionEndTime = millis();        // Reset the time since motion was detected
  }

  // If the LED is on and 10 seconds have passed without motion OR 120 seconds have passed
  if (ledOn && ((millis() - motionEndTime > ledTurnOffDelay) || (millis() - motionEndTime > ledMaxOnTime))) {
    digitalWrite(ledPin, LOW);       // Turn off LED
    ledOn = false;                   // Reset LED flag
  }

  // Small delay to stabilize the readings
  delay(100);
}
