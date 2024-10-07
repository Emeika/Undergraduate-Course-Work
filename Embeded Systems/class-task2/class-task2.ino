
/*
 * simpleSwitchWithSevenSegment-1.ino
 * Single 7-segment counter with a switch
 * Common anode 7-segment
 * 
 * Without switch debounce
 * Left as an exercise for studnets
 */

// Arduino digital pins used to light up
// corresponding segments on the LED display

long randNumber;

#define A 2
#define B 3
#define C 4
#define D 5
#define E 6
#define F_SEG 7
#define G 8

// Pushbutton connected to pin 9
#define BUTTON 12

// Common anode;
// on when pin is low
// and off when pin is high
#define ON HIGH
#define OFF LOW

//int count = 0; // current display count
int val = 0;   // digital input from button

void setup() {
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F_SEG, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(BUTTON, INPUT);
}

int randomGenerator()
{
  return random(1, 7);
}

void loop() {
  val = digitalRead(BUTTON);
  if (val == HIGH) 
  {
    int num = randomGenerator();

    switch (num) 
    {
      case 0:
        zero();
        break;
      case 1:
        one();
        break;
      case 2:
        two();
        break;
      case 3:
        three();
        break;
      case 4:
        four();
        break;
      case 5:
        five();
        break;
      case 6:
        six();
        break;
      case 7:
        seven();
        break;
      case 8:
        eight();
        break;
      case 9:
        nine();
        break;
    }

    delay(10000);
    off();
  }
}


void off()
{
  digitalWrite(A, OFF);
  digitalWrite(B, OFF);
  digitalWrite(C, OFF);
  digitalWrite(D, OFF);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, OFF);
  digitalWrite(G, OFF);

}

//0 => ABCDEF
void zero() {
  digitalWrite(A, ON);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, ON);
  digitalWrite(E, ON);
  digitalWrite(F_SEG, ON);
  digitalWrite(G, OFF);
}

// 1 => BC
void one() {
  digitalWrite(A, OFF);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, OFF);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, OFF);
  digitalWrite(G, OFF);
}

// 2 => ABDEG
void two() {
  digitalWrite(A, ON);
  digitalWrite(B, ON);
  digitalWrite(C, OFF);
  digitalWrite(D, ON);
  digitalWrite(E, ON);
  digitalWrite(F_SEG, OFF);
  digitalWrite(G, ON);
}

// 3 => ABCDG
void three() {
  digitalWrite(A, ON);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, ON);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, OFF);
  digitalWrite(G, ON);
}

// 4 => BCFG
void four() {
  digitalWrite(A, OFF);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, OFF);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, ON);
  digitalWrite(G, ON);
}

// 5 => ACDFG
void five() {
  digitalWrite(A, ON);
  digitalWrite(B, OFF);
  digitalWrite(C, ON);
  digitalWrite(D, ON);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, ON);
  digitalWrite(G, ON);
}

// 6 => ACDEFG
void six() {
  digitalWrite(A, ON);
  digitalWrite(B, OFF);
  digitalWrite(C, ON);
  digitalWrite(D, ON);
  digitalWrite(E, ON);
  digitalWrite(F_SEG, ON);
  digitalWrite(G, ON);
}

// 7 => ABC
void seven() {
  digitalWrite(A, ON);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, OFF);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, OFF);
  digitalWrite(G, OFF);
}

// 8 => ABCDEFG
void eight() {
  digitalWrite(A, ON);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, ON);
  digitalWrite(E, ON);
  digitalWrite(F_SEG, ON);
  digitalWrite(G, ON);
}

// 9 => ABCDFG
void nine() {
  digitalWrite(A, ON);
  digitalWrite(B, ON);
  digitalWrite(C, ON);
  digitalWrite(D, ON);
  digitalWrite(E, OFF);
  digitalWrite(F_SEG, ON);
  digitalWrite(G, ON);
}
