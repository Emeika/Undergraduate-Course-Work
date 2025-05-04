#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "yourSSID";
const char* password = "yourPassword";
WebServer server(80);

int leds[] = {23, 22, 21, 19}; // Define LED GPIO pins
int numLeds = sizeof(leds) / sizeof(leds[0]);

void setup() {
  Serial.begin(115200);

  // Initialize LED pins
  for (int i = 0; i < numLeds; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/control", handleControl);

  server.begin();
  Serial.println("Server started");
}

void loop() {
  server.handleClient();
}

void handleRoot() {
  String page = "<html><body>";
  page += "<h1>LED Control</h1>";
  page += "<form action='/control' method='GET'>";
  page += "<select name='action'>";
  page += "<option value='binary'>Binary Counter</option>";
  page += "<option value='shiftleft'>Shift Left</option>";
  page += "<option value='shiftright'>Shift Right</option>";
  page += "</select>";
  page += "<button type='submit'>Submit</button>";
  page += "</form></body></html>";

  server.send(200, "text/html", page);
}

void handleControl() {
  String action = server.arg("action");

  if (action == "binary") {
    binaryCounter();
  } else if (action == "shiftleft") {
    shiftLeft();
  } else if (action == "shiftright") {
    shiftRight();
  }

  server.send(200, "text/plain", "Action performed: " + action);
}

void binaryCounter() {
  for (int i = 0; i < (1 << numLeds); i++) {
    for (int j = 0; j < numLeds; j++) {
      digitalWrite(leds[j], (i >> j) & 1);
    }
    delay(500);
  }
}

void shiftLeft() {
  for (int i = 0; i < numLeds; i++) {
    for (int j = 0; j < numLeds; j++) {
      digitalWrite(leds[j], (j == i) ? HIGH : LOW);
    }
    delay(500);
  }
}

void shiftRight() {
  for (int i = numLeds - 1; i >= 0; i--) {
    for (int j = 0; j < numLeds; j++) {
      digitalWrite(leds[j], (j == i) ? HIGH : LOW);
    }
    delay(500);
  }
}
