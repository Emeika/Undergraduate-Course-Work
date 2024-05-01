#include <stdio.h>
#include <stdlib.h>

void displayFile(const char *sourceFile);
void detectSlashComments(const char *sourceFile);
void detectStarComments(const char *sourceFile);

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        printf("Usage: %s <sourceFile1.c> <sourceFile2.c>\n", argv[0]);
        return 1;
    }

    detectSlashComments(argv[1]);
    printf("\n");
    detectStarComments(argv[2]);
}

void displayFile(const char *sourceFile)
{
    FILE *readFile = fopen(sourceFile, "r");
    if (readFile == NULL)
    {
        perror("Failed to open file");
        return;
    }
    int c;

    while ((c = fgetc(readFile)) != EOF)
    {
        printf("%c", c);
    }

    printf("\n");
    fclose(readFile);
}

void detectSlashComments(const char *sourceFile)
{
    printf("Source file: %s\n", sourceFile);
    displayFile(sourceFile);

    FILE *readFile = fopen(sourceFile, "r");
    if (readFile == NULL)
    {
        perror("Failed to open file");
        return;
    }

    char buffer[256];
    int line = 1;

    printf("\n");
    while (fgets(buffer, 256, readFile) != NULL)
    {
        for (int i = 0; buffer[i] != '\0'; i++)
        {
            if (buffer[i] == '/' && buffer[i + 1] == '/')
            {
                printf("Line Number: %d         A double slash comment found\n", line);
            }
        }

        line++;
    }

    fclose(readFile);
}

void detectStarComments(const char *sourceFile)
{
    printf("Source file: %s\n", sourceFile);
    displayFile(sourceFile);

    FILE *readFile = fopen(sourceFile, "r");
    if (readFile == NULL)
    {
        perror("Failed to open file");
        return;
    }

    char buffer[256];
    int openingStack[256];
    int stackPointer = 0;
    int line = 1;

    printf("\n");
    while (fgets(buffer, 256, readFile) != NULL)
    {
        for (int i = 0; buffer[i] != '\0'; i++)
        {
            if (buffer[i] == '/' && buffer[i + 1] == '*')
            {
                printf("Opening symbol found in line %d\n", line);
                openingStack[stackPointer] = line;
                stackPointer++;
                i++;
            }
            else if (buffer[i] == '*' && buffer[i + 1] == '/')
            {
                if (stackPointer != 0)
                {
                    int openingNumber = openingStack[stackPointer - 1];
                    printf("Closing symbol against opening symbol in line %d found in line %d\n", openingNumber, line);
                    stackPointer--;
                }

                i++;
            }
        }

        line++;
    }

    if (openingStack[0] != 0)
    {
        printf("Closing symbol against opening symbol for line");
        for (int i = 0; i < stackPointer; i++)
        {
            printf(" %d", openingStack[i]);
            if (i + 1 != stackPointer)
            {
                printf(", and");
            }
        }
        printf(" not found\n");
    }

    fclose(readFile);
}
