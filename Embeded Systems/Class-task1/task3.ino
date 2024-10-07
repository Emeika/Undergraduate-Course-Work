int incomingByte = 0; // for incoming serial data
int arr[4];
int arr2[4];

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  get_array(arr, 4);
  display_array(arr, 4);
  reverse_array(arr, arr2, 4);
  display_array(arr2, 4);
}

void loop() {
}

void get_array(int array[], int size)
{
  int i = 0;
  while (i < size)
  {
    if (Serial.available() > 0)
    {
      incomingByte = Serial.read();

      // ignore \n
      if (incomingByte != 10)
      {
        array[i] = incomingByte;
        i++;
      }
    }
  }
}

void reverse_array(int array1[], int array2[], int size)
{
  for (int i = 0; i < size; i++)
  {
    array2[size - 1 - i] = array1[i];
  }
}

void display_array(int array[], int size)
{
  for (int i = 0; i < size; i++)
  {
    Serial.print(array[i]);
    Serial.print(" ");
  }
  Serial.println();
}
