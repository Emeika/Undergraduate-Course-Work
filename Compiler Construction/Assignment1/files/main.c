/*
Name: Hafsah Shahbaz
Roll Number: 251684784
*/

#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 2024
#define MAX_LINES 2024
#define MAX_MACROS 10

typedef struct
{
    char name[MAX_LINE_LENGTH];
    char value[MAX_LINE_LENGTH];
} Macro;

void removeBlankLines(const char *inputFile);
void removeComments(const char *withoutBlankLinesFile);
void macroExpansion(const char *withoutCommentsFile);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <inFile.c>\n", argv[0]);
        return 1;
    }
    removeBlankLines(argv[1]);
    removeComments("withoutBlankLinesFile.c");
    macroExpansion("withoutCommentsFile.c");

    FILE *outFile = fopen("out.c", "r");
    if (outFile == NULL)
    {
        perror("Failed to open output file");
        return 1;
    }
    printf("\nFile processed successfully: \n");

    int c;

    while ((c = fgetc(outFile)) != EOF)
    {
        printf("%c", c);
    }
    fclose(outFile);

    return 0;
}

void removeBlankLines(const char *inputFile)
{
    FILE *readFile = fopen(inputFile, "r");
    FILE *writeFile = fopen("withoutBlankLinesFile.c", "w");

    if (readFile == NULL || writeFile == NULL)
    {
        perror("Failed to open file");
        return;
    }

    char ch;
    char buffer[MAX_LINES][MAX_LINE_LENGTH];
    int line_count = 0;

    while ((fgets(buffer[line_count], MAX_LINE_LENGTH, readFile)) != NULL)
    {
        if (buffer[line_count][0] != '\n' && buffer[line_count][0] != '\0')
        {
            line_count++;
            if (line_count >= MAX_LINES)
            {
                fprintf(stderr, "Reached maximum number of lines\n");
                break;
            }
        }
    }

    for (int i = 0; i < line_count; i++)
    {
        fprintf(writeFile, "%s", buffer[i]);
    }

    fclose(readFile);
    fclose(writeFile);
}

void removeComments(const char *withoutBlankLinesFile)
{
    FILE *readFile = fopen(withoutBlankLinesFile, "r");
    FILE *writeFile = fopen("withoutCommentsFile.c", "w");

    if (readFile == NULL || writeFile == NULL)
    {
        perror("Failed to open file");
        return;
    }

    // if curent c is  and previous c is slash then go to \n, dont write in file the remaining untill /n
    // if a slash and next char is * then keep reading character untill current c is / (dont write this in file)

    char prevChar = fgetc(readFile);
    char currChar;
    int incomment = 0;
    while ((currChar = fgetc(readFile)) != EOF)
    {
        if (prevChar == '/' && currChar == '*')
        {
            while (!(prevChar == '*' && currChar == '/'))
            {
                prevChar = currChar;
                currChar = fgetc(readFile);
                if (currChar == EOF)
                    break;
            }
            if (currChar == EOF)
                break;

            prevChar = fgetc(readFile);
            prevChar = fgetc(readFile);

            continue;
        }
        if (prevChar == '/' && currChar == '/')
        {
            while ((currChar = fgetc(readFile)) != '\n' && currChar != EOF)
                ;
            prevChar = fgetc(readFile);
            // prevChar = currChar;
            if (currChar == EOF)
                break;
            continue;
        }
        fputc(prevChar, writeFile);
        prevChar = currChar;
    }
    if (prevChar != EOF)
    {
        fputc(prevChar, writeFile);
    }

    fclose(readFile);
    fclose(writeFile);
}

void macroExpansion(const char *withoutCommentsFile)
{
    FILE *readFile = fopen(withoutCommentsFile, "r");
    FILE *writeFile = fopen("out.c", "w");
    FILE *tempFile = fopen("temp.txt", "w+");

    if (readFile == NULL || writeFile == NULL || tempFile == NULL)
    {
        perror("Failed to open file");
        return;
    }

    char buffer[MAX_LINE_LENGTH];
    Macro macros[MAX_MACROS];
    int macrosFound = 0;

    while (fgets(buffer, MAX_LINE_LENGTH, readFile) != NULL)
    {
        if (buffer[0] == '#' && buffer[1] == 'd' && buffer[2] == 'e' && buffer[3] == 'f' && buffer[4] == 'i' && buffer[5] == 'n' && buffer[6] == 'e')
        {

            int i = 7;
            while (buffer[i] == ' ')
            {
                i++;
            }

            int j = 0;
            while (buffer[i] != ' ' && buffer[i] != '\n')
            {
                macros[macrosFound].name[j++] = buffer[i++];
            }
            macros[macrosFound].name[j] = '\0';

            while (buffer[i] == ' ')
            {
                i++;
            }

            j = 0;
            while (buffer[i] != '\n')
            {
                macros[macrosFound].value[j++] = buffer[i++];
            }
            macros[macrosFound].value[j] = '\0';
            macrosFound++;

            // printf("Macro Name: %s, Value: %s\n", macros[macrosFound-1].name, macros[macrosFound-1].value);
        }
        else
        {
            fputs(buffer, tempFile);
        }
    }

    rewind(tempFile);

    if (macrosFound)
    {
        while (fgets(buffer, MAX_LINE_LENGTH, tempFile) != NULL)
        {
            int i = 0;
            while (buffer[i] != '\0')
            {
                int foundMacro = 0;
                for (int k = 0; k < macrosFound; k++)
                {
                    int match = 1;
                    int l;
                    for (l = 0; macros[k].name[l] != '\0'; l++)
                    {
                        if (macros[k].name[l] != buffer[i + l])
                        {
                            match = 0;
                            break;
                        }
                    }
                    if (match)
                    {
                        foundMacro = 1;
                        fputs(macros[k].value, writeFile);
                        i += l;
                        break;
                    }
                }
                if (!foundMacro)
                {
                    fputc(buffer[i], writeFile);
                    i++;
                }
            }
        }
    }
    else
    {
        while (fgets(buffer, MAX_LINE_LENGTH, tempFile) != NULL)
        {
            fputs(buffer, writeFile);
        }
    }

    fclose(readFile);
    fclose(writeFile);
    fclose(tempFile);
}
