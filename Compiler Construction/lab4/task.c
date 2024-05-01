#include <stdio.h>
#include <stdlib.h>

void addLineNumber(char *inFile, char *inFileWithLineNo);
void removeBlankLines(char *inFileWithLineNo, char *inFileWithoutBlanks);
void displayFile(char *filename);

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Usage: %s <inFile> <inFileWithLineNo> <inFileWithoutBlanks>\n", argv[0]);
        return 1;
    }

    FILE *fp3 = fopen(argv[3], "w");
    if (fp3 == NULL)
    {
        printf("Couldn't open %s\n", argv[3]);
        return 1;
    }

    addLineNumber(argv[1], argv[2]);
    removeBlankLines(argv[2], argv[3]);
    printf("\n=====ORIGINAL FILE=====\n");
    displayFile(argv[1]);
    printf("\n\n====FILE WITH LINE NUMBER=====\n");
    displayFile(argv[2]);
    printf("\n\n====FILE WITHOUT BLANK LINES=====\n");
    displayFile(argv[3]);

    return 0;
}

void addLineNumber(char *inFile, char *inFileWithLineNo)
{
    FILE *readFile = fopen(inFile, "r");
    if (readFile == NULL)
    {
        printf("Couldn't open %s\n", inFile);
        exit(1);
    }

    FILE *lineFile = fopen(inFileWithLineNo, "w");
    if (lineFile == NULL)
    {
        printf("Couldn't open %s\n", inFileWithLineNo);
        exit(1);
    }

    int lineNum = 1;
    char ch;
    do
    {
        ch = fgetc(readFile);

        if (feof(readFile))
        {
            break;
        }

        if (lineNum == 1)
        {
            fprintf(lineFile, "%d. ", lineNum);
            lineNum++;
        }

        if (ch == '\n')
        {
            fprintf(lineFile, "\n%d. ", lineNum);
            lineNum += 1;
        }
        else
        {
            fprintf(lineFile, "%c", ch);
        }

    } while (1);

    fclose(readFile);
    fclose(lineFile);
}

void removeBlankLines(char *inFileWithLineNo, char *inFileWithoutBlanks)
{
    FILE *readFile = fopen(inFileWithLineNo, "r");
    if (readFile == NULL)
    {
        printf("Couldn't open %s\n", inFileWithLineNo);
        exit(1);
    }

    FILE *blankFile = fopen(inFileWithoutBlanks, "w");
    if (blankFile == NULL)
    {
        printf("Couldn't open %s\n", inFileWithoutBlanks);
        exit(1);
    }

    char ch;
    char lineNum = '1';
    int charCount = 0;
    int line = 1;

    do
    {
        ch = fgetc(readFile);
        charCount++;

        if (feof(readFile))
        {
            break;
        }

        if (charCount == 4 && ch == '\n')
        {
            charCount = 3;
            fseek(readFile, 3, SEEK_CUR);
            continue;
        }

        if (ch == '\n')
        {
            charCount = 0;
        }

        if (ch == '5')
        {
            ch = '3';
        }

        if (ch == '8')
        {
            ch = '4';
        }
        fprintf(blankFile, "%c", ch);
    } while (1);

    fclose(readFile);
    fclose(blankFile);
}

void displayFile(char *filename)
{
    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("Couldn't open file\n");
        exit(1);
    }

    char ch;
    do
    {
        ch = fgetc(fp);
        printf("%c", ch);
    } while (ch != EOF);
    fclose(fp);
}
