#include <WiFi.h>
#include <HTTPClient.h>
#include "time.h"

// Wi-Fi Credentials
const char* ssid = "Lounge";
const char* password = "redbrown7";

// Google Apps Script Web App URL
String GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx2Kq1hCSFCXOu_YhH3fTVYK8lvnMl4vweANUtDDOC5BvQhBTQuhPxibl_fDesxZ_685Q/exec";

// GPIO Pins for LEDs
#define LED1 2
#define LED2 4
#define LED3 18
#define LED4 19

// GPIO Pins for Buttons
#define BUTTON1 26
#define BUTTON2 25
#define BUTTON3 33
#define BUTTON4 32

// NTP Time Configuration
const char* ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 3600 * 5; // Adjust for your timezone (e.g., GMT+5)
const int daylightOffset_sec = 0;

// Variables to Track LED States
bool ledState1 = false;
bool ledState2 = false;
bool ledState3 = false;
bool ledState4 = false;

// Variables to Track Previous States for Debounce
bool lastButtonState1 = HIGH;
bool lastButtonState2 = HIGH;
bool lastButtonState3 = HIGH;
bool lastButtonState4 = HIGH;

// Debounce Timing
unsigned long lastDebounceTime1 = 0;
unsigned long lastDebounceTime2 = 0;
unsigned long lastDebounceTime3 = 0;
unsigned long lastDebounceTime4 = 0;
unsigned long debounceDelay = 50;

// Function to Upload LED State to Google Sheet
void uploadToGoogleSheet(int led, bool state) {
  if (WiFi.status() == WL_CONNECTED) {
    struct tm timeinfo;
    if (!getLocalTime(&timeinfo)) {
      Serial.println("Failed to obtain time");
      return;
    }

    char dateBuffer[11]; // YYYY-MM-DD
    strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", &timeinfo);

    char timeBuffer[9]; // HH:MM:SS
    strftime(timeBuffer, sizeof(timeBuffer), "%H:%M:%S", &timeinfo);

    String url = GOOGLE_SCRIPT_URL + "?led=" + String(led) +
                 "&status=" + String(state ? "ON" : "OFF") +
                 "&date=" + String(dateBuffer) +
                 "&time=" + String(timeBuffer);

    HTTPClient http;
    http.begin(url);
    int httpCode = http.GET();

    if (httpCode > 0) {
      String response = http.getString();
      Serial.println("Response: " + response);
    } else {
      Serial.println("Error in HTTP request");
    }

    http.end();
  } else {
    Serial.println("WiFi Disconnected!");
  }
}

void setup() {
  Serial.begin(115200);

  // Setup LEDs as Outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);

  // Setup Buttons as Inputs with Pullup Resistors
  pinMode(BUTTON1, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);
  pinMode(BUTTON4, INPUT_PULLUP);

  // Connect to Wi-Fi
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected");

  // Configure NTP Time
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
}

void loop() {
  // Read Button States
  bool buttonState1 = digitalRead(BUTTON1);
  bool buttonState2 = digitalRead(BUTTON2);
  bool buttonState3 = digitalRead(BUTTON3);
  bool buttonState4 = digitalRead(BUTTON4);

  unsigned long currentTime = millis();

  // Handle Button 1
  if (buttonState1 != lastButtonState1 && (currentTime - lastDebounceTime1 > debounceDelay)) {
    lastDebounceTime1 = currentTime;
    if (buttonState1 == LOW) { // Button Pressed
      ledState1 = !ledState1; // Toggle LED State
      digitalWrite(LED1, ledState1 ? HIGH : LOW);
      uploadToGoogleSheet(1, ledState1);
    }
  }
  lastButtonState1 = buttonState1;

  // Handle Button 2
  if (buttonState2 != lastButtonState2 && (currentTime - lastDebounceTime2 > debounceDelay)) {
    lastDebounceTime2 = currentTime;
    if (buttonState2 == LOW) {
      ledState2 = !ledState2;
      digitalWrite(LED2, ledState2 ? HIGH : LOW);
      uploadToGoogleSheet(2, ledState2);
    }
  }
  lastButtonState2 = buttonState2;

  // Handle Button 3
  if (buttonState3 != lastButtonState3 && (currentTime - lastDebounceTime3 > debounceDelay)) {
    lastDebounceTime3 = currentTime;
    if (buttonState3 == LOW) {
      ledState3 = !ledState3;
      digitalWrite(LED3, ledState3 ? HIGH : LOW);
      uploadToGoogleSheet(3, ledState3);
    }
  }
  lastButtonState3 = buttonState3;

  // Handle Button 4
  if (buttonState4 != lastButtonState4 && (currentTime - lastDebounceTime4 > debounceDelay)) {
    lastDebounceTime4 = currentTime;
    if (buttonState4 == LOW) {
      ledState4 = !ledState4;
      digitalWrite(LED4, ledState4 ? HIGH : LOW);
      uploadToGoogleSheet(4, ledState4);
    }
  }
  lastButtonState4 = buttonState4;
}
