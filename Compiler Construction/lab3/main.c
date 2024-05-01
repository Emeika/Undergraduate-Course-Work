/*
Lab 3
Daim Bin Khalid 251686775
Hafsah Shahbaz 251684784
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: lab3 <filename>\n");
        return 1;
    }

    // file to clear extra spaces
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Error opening file %s\n", argv[1]);
        return 1;
    }

    // file to write to
    FILE *outfile = fopen("output.txt", "w");
    if (outfile == NULL)
    {
        printf("Error opening file output.txt\n");
        return 1;
    }

    char *word = NULL;
    char character;
    size_t word_len = 0;
    int lastWhiteSpace = 0;

    do
    {
        character = fgetc(infile);

        if (feof(infile))
        {
            if (word_len > 0)
            {
                // write the last word to outfile
                fwrite(word, sizeof(char), word_len, outfile);
            }

            break;
        }

        // if (character == ';' && lastWhiteSpace)
        // {
        //     fseek(outfile, -1, SEEK_CUR);
        //     fputc(character, outfile);
        //     lastWhiteSpace = 0;
        //     continue;
        // }

        if (character != ' ' && character != '\t' && character != '\r')
        {
            word_len++;
            word = realloc(word, word_len * sizeof(char));
            if (word == NULL)
            {
                printf("Memory allocation failed\n");
                return 1;
            }

            word[word_len - 1] = character;
        }
        else
        {
            if (word_len > 0)
            {
                fwrite(word, sizeof(char), word_len, outfile);
                fputc(' ', outfile);
                lastWhiteSpace = 1;

                free(word);
                word = NULL;
                word_len = 0;
            }
        }
    } while (1);

    fclose(infile);
    fclose(outfile);
    printf("Done\n");

    return 0;
}
