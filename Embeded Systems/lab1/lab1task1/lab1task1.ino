// Lab 1 - Embedded Systems
// Daim Bin Khalid - 251686775
// Hafsah Shahbaz - 251684784

int getNumber();
int getSize();
void displayArray(int arr[], int size);
void populateArray(int arr[], int size);
float getDecimalValue(int arr[], int size);
void getComplement(int arr[], int complNumber[], int size);
int getBitPos();
int readBit(int arr[], int size, int p);

int size;
char n;
char arr[5];
int num;

void setup()
{
    Serial.begin(9600);
    Serial.println("\t=====LAB 01=====");
    Serial.println();

    // get array size
    Serial.print("Enter size of array: ");
    size = getSize();
    Serial.println(size);
    int binNumber[size];
    int complNumber[size];

    Serial.println("Enter binary values in the array: ");
    populateArray(binNumber, size);
    Serial.println("Binary number entered is: ");
    displayArray(binNumber, size);

    Serial.print("Decimal value of this binary number is: ");
    float decValue = getDecimalValue(binNumber, size);
    Serial.println(decValue);
    Serial.print("Complement of given binary number is: ");
    getComplement(binNumber, complNumber, size);
    displayArray(complNumber, size);
    Serial.print("Enter a bit position (Position of LS Bit being 0): ");
    int pos = getBitPos();
    Serial.println(pos);
    Serial.print("The binary value of digit at position ");
    Serial.print(pos);
    Serial.print(" is ");
    int binVal = readBit(binNumber, size, pos);
    Serial.println(binVal);
}

void loop()
{
}

int getNumber()
{
}

int getSize()
{
    while (Serial.available() == 0)
    {
    }

    String input = Serial.readStringUntil('\n');
    int size = input.toInt();
    return size;
}

void populateArray(int arr[], int size)
{
    int i = 0;
    while (i < size)
    {
        while (Serial.available() == 0)
        {
        }

        int num = Serial.read();
        if (num == '0' || num == '1')
        {
            // convert from ASCII to binary (0 or 1)
            arr[i] = num - '0';
            i++;
        }
    }
}

void displayArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        Serial.print(arr[i]);
        Serial.print(" ");
    }
    Serial.println();
}

float getDecimalValue(int arr[], int size)
{
    float decimalValue = 0;

    for (int i = 0; i < size; i++)
    {
        // mult each binary digit by the corresponding power of 2
        decimalValue += arr[i] * pow(2, size - 1 - i);
    }

    return decimalValue;
}

void getComplement(int arr[], int complNumber[], int size)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == 0)
        {
            complNumber[i] = 1;
        }
        else complNumber[i] = 0;
    }
}

int getBitPos()
{
    while (Serial.available() == 0)
    {
    }

    String input = Serial.readStringUntil('\n');
    int size = input.toInt();
    return size;
}

int readBit(int arr[], int size, int p)
{
    return arr[size - 1 - p];
}
