#include <stdio.h>
#include <stdlib.h>
#include "preprocessor.h"

void removeBlankLines(const char *inputFile)
{
    FILE *readFile = fopen(inputFile, "r");
    FILE *writeFile = fopen("../files/withoutBlankLinesFile.c", "w");

    if (readFile == NULL)
    {
        perror("Failed to open input file");
        return;
    }
    if (writeFile == NULL)
    {
        perror("Failed to open output file");
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

void removeComments()
{
    FILE *readFile = fopen("../files/withoutBlankLinesFile.c", "r");
    FILE *writeFile = fopen("../files/withoutCommentsFile.c", "w");

    if (readFile == NULL)
    {
        perror("Failed to open withoutBlankLinesFile");
        return;
    }
    if (writeFile == NULL)
    {
        perror("Failed to open withoutCommentsFile");
        return;
    }

    // char buffer[MAX_LINE_LENGTH];
    // int insideComment = 0; // Flag to track if we're inside a /* */ comment

    // while (fgets(buffer, MAX_LINE_LENGTH, readFile) != NULL) {
    //     printf("Original line: %s", buffer);
    //     int i = 0;
    //     while (buffer[i] != '\0') {
    //         if (!insideComment && buffer[i] == '/' && buffer[i + 1] == '/') {
    //             printf("Single-line comment found, breaking loop\n");
    //             // If single-line comment found, terminate the buffer at this point
    //             buffer[i] = '\0';
    //             break;
    //         } else if (!insideComment && buffer[i] == '/' && buffer[i + 1] == '*') {
    //             printf("Start of multi-line comment found\n");
    //             // If start of multi-line comment found, set insideComment flag
    //             insideComment = 1;
    //             i++; // Move index ahead to skip '*'
    //         }
    //         else if (insideComment && buffer[i] == '*' && buffer[i + 1] == '/')
    //         {
    //             printf("End of multi-line comment found\n");
    //             // If end of multi-line comment found, unset insideComment flag
    //             insideComment = 0;
    //             i=i+2; // Move index ahead to skip '/' and '\n'
    //         }
    //         else if (!insideComment)
    //         {
    //             // Write character to output file if not inside a comment
    //             //printf("Writing character to output: %c\n", buffer[i]);
    //             fputc(buffer[i], writeFile);
    //         }
    //         i++;
    //     }
    // }

    // if curent c is  and previous c is slash then go to \n, dont write in buffer the remaining untill /n
    // if a slash and next char is * then keep reading character untill current c is / (dont write this in file)
    //
    //     /n  #

    char prevChar = fgetc(readFile);
    char currChar;
    int incomment = 0;
    while((currChar = fgetc(readFile)) != EOF)
    {
        //printf("prev %c \n", prevChar);
        //printf("cur %c \n", currChar);
        if (prevChar == '/' && currChar == '*')
        {
            while(!(prevChar == '*' && currChar == '/'))
            {
                prevChar = currChar;
                currChar = fgetc(readFile);
                if (currChar == EOF) break;
            }
            if (currChar == EOF) break;

            prevChar = fgetc(readFile);
            prevChar = fgetc(readFile);

            continue;
        }

        if (prevChar == '/' && currChar == '/')
        {
            while ((currChar = fgetc(readFile)) != '\n' && currChar != EOF);
            prevChar = fgetc(readFile);
            //prevChar = currChar;
            if (currChar == EOF) break;
            continue;

        }
        fputc(prevChar, writeFile);
        prevChar = currChar;
    }
    if (prevChar != EOF) {
        fputc(prevChar, writeFile);
    }
    fclose(readFile);
    fclose(writeFile);

}

void macroExpansion(const char *macroFile)
{
    FILE *readFile = fopen(macroFile, "r");
    FILE *writeFile = fopen("../files/out.c", "w");
    FILE *tempFile = fopen("../files/temp.txt", "w+");

    if (readFile == NULL || writeFile == NULL || tempFile == NULL)
    {
        perror("Error opening file");
        return;
    }

    char buffer[MAX_LINE_LENGTH];
    Macro macros[MAX_MACROS];
    int macrosFound = 0;

    while (fgets(buffer, MAX_LINE_LENGTH, readFile) != NULL) {
        // Check for macro definitions
        if (buffer[0] == '#' && buffer[1] == 'd' && buffer[2] == 'e' && buffer[3] == 'f' && buffer[4] == 'i' && buffer[5] == 'n' && buffer[6] == 'e') {

            int i = 7;
            while (buffer[i] == ' ') {
                i++;
            }

            // Extract macro name
            int j = 0;
            while (buffer[i] != ' ' && buffer[i] != '\n') {
                macros[macrosFound].name[j++] = buffer[i++];
            }
            macros[macrosFound].name[j] = '\0'; // Null-terminate the macro name

            // Find the start of macro value
            while (buffer[i] == ' ') {
                i++;
            }

            // Extract macro value
            j = 0;
            while (buffer[i] != '\n') {
                macros[macrosFound].value[j++] = buffer[i++];
            }
            macros[macrosFound].value[j] = '\0'; // Null-terminate the macro value
            macrosFound++;

            // Process the macro (e.g., store it, use it, etc.)
            printf("Macro Name: %s, Value: %s\n", macros[macrosFound-1].name, macros[macrosFound-1].value);
        }
        else {
            fputs(buffer, tempFile);
        }
    }

    rewind(tempFile);
    buffer[0] = '\0';

    if (macrosFound) {
        while (fgets(buffer, MAX_LINE_LENGTH, tempFile) != NULL) {
            int i = 0;
            while (buffer[i] != '\0') {
                int foundMacro = 0;
                for (int k = 0; k < macrosFound; k++) {
                    int match = 1;
                    int l;
                    for (l = 0; macros[k].name[l] != '\0'; l++) {
                        if (macros[k].name[l] != buffer[i + l]) {
                            match = 0;
                            break;
                        }
                    }
                    if (match) {
                        foundMacro = 1;
                        printf("Found macro: %s\n", macros[k].name);
                        printf("Replacing macro: %s\n", macros[k].name);
                        fputs(macros[k].value, writeFile);
                        i += l; // Move to after the replaced macro
                        break;
                    }
                }
                if (!foundMacro) {
                    fputc(buffer[i], writeFile);
                    i++;
                }
            }
        }
    }
    else {
        rewind(tempFile);
        while (fgets(buffer, MAX_LINE_LENGTH, tempFile) != NULL) {
            fputs(buffer, writeFile);
        }
    }
    fclose(readFile);
    fclose(writeFile);
    fclose(tempFile);
}
