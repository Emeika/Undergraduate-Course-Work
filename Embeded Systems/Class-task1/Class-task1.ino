int readPin[] = {7,8,9,10};
int readPin7 = 5;
void setup() {
  //Serial.begin(9600);
  

    pinMode(readPin7, OUTPUT);

  
}

void displayDigit(byte digit)
{
  for (int i = 0; i<4; i++)
  {
    if (bitRead(digit, i) == 1)
    {
      digitalWrite(readPin[i], HIGH);
    }
    else {digitalWrite(readPin[i], LOW);  }  
  }
}

void loop()
{
  digitalWrite(readPin7, HIGH);

}
