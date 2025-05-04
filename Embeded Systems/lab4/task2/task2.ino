#include "SimpleArduinoEncryption.h"

const byte ENCRYPTION_KEYS[] = {0xAA, 0xBB, 0xCC, 0xCB};
const size_t NUM_KEYS = sizeof(ENCRYPTION_KEYS) / sizeof(ENCRYPTION_KEYS[0]);

SimpleArduinoEncryption encryption(ENCRYPTION_KEYS, NUM_KEYS);

void setup() {
  Serial.begin(9600);
  
  while (Serial.available() == 0)
  {}
  String input = Serial.readString();
  Serial.print("Original String: ");
  Serial.println(input);

  // Encryption
  size_t length = input.length();
  char message[length + 1];
  input.toCharArray(message, sizeof(message));

  encryption.encrypt(message);

  char hexStr[length * 2 + 1];
  SimpleArduinoEncryption::bytesToHex((const byte*)message, length, hexStr);

  Serial.print("Encrypted String (Hex): ");
  Serial.println(hexStr);

  // Decryption
  size_t length2 = strlen(hexStr) / 2;
  byte message2[length2 + 1];

  SimpleArduinoEncryption::hexToBytes(hexStr, message2, length2);
  message2[length2] = '\0';

  encryption.decrypt((char*)message2);
  String decryptedString = String((char*)message2);

  Serial.print("Decrypted String: ");
  Serial.println(decryptedString);
}

void loop() {
}
