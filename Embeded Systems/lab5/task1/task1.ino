int ledPin = 13;                // LED 
int pirPin = 2;                 // PIR Out pin 
int pirStat = 0;                   // PIR status

void setup() {
 pinMode(ledPin, OUTPUT);     
 pinMode(pirPin, INPUT);     
 Serial.begin(9600);
}

void loop(){
 pirStat = digitalRead(pirPin); 
 if (pirStat == LOW) {
   digitalWrite(ledPin, LOW);  // turn LED off
   Serial.println("No Motion");
 } 
 else {
   digitalWrite(ledPin, HIGH); // turn LED on
   Serial.println("Motion Detected");
 }
}
