#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: lab3 <filename> \n");
        return 1;
    }

    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Error opening file %s\n", argv[1]);
        return 1;
    }
    FILE *outfile = fopen("output.txt", "w");
    if (outfile == NULL)
    {
        printf("Error opening file output.txt\n");
        return 1;
    }

    char ch;
    char next_ch;
    int space = 0;

    ch = fgetc(infile);

    while (ch != EOF)
    {
        next_ch = fgetc(infile);

        if (ch != '\n' && ch != '\t' && ch != '\r')
        {
            if (ch == ' ')
            {
                if (next_ch != ';')
                {
                    space += 1;
                    if (space == 1)
                    {
                        fputc(ch, outfile);
                    }
                }
                else
                {
                    fseek(outfile, -1, SEEK_CUR);
                }
            }
            else
            {
                space = 0;
                fputc(ch, outfile);
            }
        }
        else
        {
            fputc(ch, outfile);
        }

        ch = next_ch;
    }

    fclose(infile);
    fclose(outfile);
    return 0;
}
