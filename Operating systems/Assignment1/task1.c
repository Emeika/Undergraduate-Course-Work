#include <stdio.h>
#include <string.h>

// #include <stdlib.h>  //for atoi
int main()
{
    char input[100];
    printf("Enter ascii characters: ");

    fgets(input, 100, stdin); // Read input from the user

    // Tokenize the input based on space and comma delimiters
    char *token = strtok(input, " ,");

    while (token != NULL)
    {
        int ascii;
        sscanf(token, "%d", &ascii); // int ascii = atoi(token);
        printf("%c", ascii);
        token = strtok(NULL, " ,"); // Move to the next token
    }
    return 0;
}