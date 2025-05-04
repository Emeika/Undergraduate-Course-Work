char receivedCommand; // To store the command received via Bluetooth
int relayPin = 8;     // Pin connected to the relay IN terminal

void setup() {
  pinMode(relayPin, OUTPUT);  // Set relay pin as output
  digitalWrite(relayPin, LOW); // Ensure relay starts in OFF state

  Serial.begin(9600); // Initialize serial communication for Bluetooth
  Serial.println("Ready to receive commands via Bluetooth!");
}

void loop() {
  // Check if data is available on the Bluetooth connection
  if (Serial.available() > 0) {
    receivedCommand = Serial.read(); // Read the incoming command
    
    if (receivedCommand == '1') {
      digitalWrite(relayPin, HIGH); // Turn ON the relay
      Serial.println("Relay ON (LED ON)");
    } 
    else if (receivedCommand == '0') {
      digitalWrite(relayPin, LOW); // Turn OFF the relay
      Serial.println("Relay OFF (LED OFF)");
    } 
  }
}
