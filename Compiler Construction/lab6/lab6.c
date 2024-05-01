/*
Lab 6
Daim Bin Khalid - 251686775
Hafsah Shahbaz - 251684784
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <path>\n", argv[0]);
        return 1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        perror("Failed to open file");
        return 1;
    }

    char *buffer = (char *)malloc(1024 * sizeof(char));
    if (buffer == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    fgets(buffer, 1024, fp);

    char *pointer = buffer;
    char *token_start = buffer;
    while (*pointer != '\0')
    {
        if (*pointer == '(')
        {
            *pointer = '\0';
            if (pointer != token_start)
            {
                printf("Word: %s\n", token_start);
            }
            printf("Open Paranthesis: (\n");
            token_start = pointer + 1;
        }

        if (*pointer == ')')
        {
            *pointer = '\0';
            if (pointer != token_start)
            {
                printf("Word: %s\n", token_start);
            }
            printf("Close Paranthesis: )\n");
            token_start = pointer + 1;
        }

        if (*pointer == '{')
        {
            *pointer = '\0';
            if (pointer != token_start)
            {
                printf("Word: %s\n", token_start);
            }
            printf("Open Curly Brace: {\n");
            token_start = pointer + 1;
        }

        if (*pointer == '}')
        {
            *pointer = '\0';
            if (pointer != token_start)
            {
                printf("Word: %s\n", token_start);
            }
            printf("Close Curly Brace: }\n");
            token_start = pointer + 1;
        }

        if (*pointer == ';')
        {
            *pointer = '\0';
            if (pointer != token_start)
            {
                printf("Word: %s\n", token_start);
            }
            printf("Semicolon: ;\n");
            token_start = pointer + 1;
        }

        if (*pointer == '"')
        {
            pointer++;
            token_start = pointer; // start of the string
            while (*pointer != '"')
            {
                pointer++;
            }
            *pointer = '\0';
            printf("String: \"%s\"\n", token_start);
            token_start = pointer + 1;
        }

        if (*pointer == ' ' || *pointer == '$')
        {
            *pointer = '\0'; // replace space with null terminator
            if (pointer != token_start)
            {
                printf("Word: %s\n", token_start);
            }
            token_start = pointer + 1; // start of next token
        }

        pointer++;
    }

    free(buffer);
    fclose(fp);
    return 0;
}
