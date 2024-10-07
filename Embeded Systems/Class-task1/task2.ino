//byte val = B10110101;
//
//const int byte_size = (8 - 1);
//
//void setup() {
//  Serial.begin(9600);
//  readBit(val);
//  readBitFour(val);
//}
//
//void loop() {
//}
//
///*this function takes a variable, prints it out bit by bit (starting from the right)
//then prints the decimal number for comparison.*/
//void readBit(long counter) {
//  Serial.print("Binary Number: ");
//  //loop through each bit
//  for (int b = byte_size; b >= 0; b--) {
//    byte bit = bitRead(counter, b);
//    Serial.print(bit);
//  }
//} 
//
//void readBitFour(long counter) {
//  Serial.println();
//  Serial.print("Flipped 4th bit Binary Number: ");
//  //loop through each bit
//  for (int b = byte_size; b >= 0; b--) {
//    byte bit = bitRead(counter, b);
//    if (b == (7-4))
//    {
//      if (bit == 0)
//      {
//        bit = 1;
//      }
//      else
//      {
//        bit = 0;
//      }
//    }
// 
//    Serial.print(bit);
//  }
//}
