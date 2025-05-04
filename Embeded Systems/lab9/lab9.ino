#include "WiFi.h"
#include <HTTPClient.h>
#include "time.h"

const char* ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 18000; // GMT+5 for Pakistan
const int daylightOffset_sec = 3600;

const char* ssid = "Galaxy A52"; // Replace with your Wi-Fi SSID
const char* password = "qwertyiu"; // Replace with your Wi-Fi password

String GOOGLE_SCRIPT_ID = "AKfycbzShLDFZD9UYHo8R5vuHoS0MDzR1WnN9UvwuyfclGQsAEto-bKF0i2Ecf0gHoIptUJyVQ"; // Replace with your Web App ID

int count = 0;

void setup() {
    Serial.begin(115200);
    delay(1000);

    // Connect to Wi-Fi
    Serial.print("Connecting to Wi-Fi: ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nConnected!");

    // Initialize time
    configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        struct tm timeinfo;
        if (!getLocalTime(&timeinfo)) {
            Serial.println("Failed to obtain time");
            return;
        }

        char timeStringBuff[50];
        strftime(timeStringBuff, sizeof(timeStringBuff), "%A, %B %d %Y %H:%M:%S", &timeinfo);
        String asString(timeStringBuff);
        asString.replace(" ", "-");

        String urlFinal = "https://script.google.com/macros/s/" + GOOGLE_SCRIPT_ID + "/exec?sensor=" + String(count) + "&date=" + asString;

        HTTPClient http;
        http.begin(urlFinal.c_str());
        int httpCode = http.GET();

        Serial.println("HTTP Status Code: " + String(httpCode));
        http.end();
    }

    count++;
    delay(2000); // Send data every 2 seconds
}
