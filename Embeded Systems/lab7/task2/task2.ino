// Define LED pins
const int led1 = 3; // 1st LED (25% volume)
const int led2 = 4; // 2nd LED (50% volume)
const int led3 = 5; // 3rd LED (75% volume)
const int led4 = 6; // 4th LED (100% volume)

void setup() {
  // Set LED pins as OUTPUT
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  // Initialize Serial Monitor for debugging
  Serial.begin(9600);
}

void loop() {
  // Read the potentiometer value (0 to 1023)
  int potValue = analogRead(A0);

  // Map potentiometer value to gas volume (0 to 100 cubic feet)
  int gasVolume = map(potValue, 0, 1023, 0, 100);

  // Turn LEDs ON/OFF based on volume
  if (gasVolume >= 25) { digitalWrite(led1, HIGH); } else { digitalWrite(led1, LOW); }
  if (gasVolume >= 50) { digitalWrite(led2, HIGH); } else { digitalWrite(led2, LOW); }
  if (gasVolume >= 75) { digitalWrite(led3, HIGH); } else { digitalWrite(led3, LOW); }
  if (gasVolume == 100) { digitalWrite(led4, HIGH); } else { digitalWrite(led4, LOW); }

  // Print to Serial Monitor for debugging
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print(" | Mapped Gas Volume: ");
  Serial.println(gasVolume);

  delay(500); // Small delay for stability
}
