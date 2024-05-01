#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("Couldn't open %s\n", argv[1]);
        return 1;
    }

    int i = 1;
    char ch;
    int char_count = 0;
    do
    {
        printf("%d: ",i);
        i += 1;

        while ((ch = fgetc(file)) != '\n')
        {
            if (ch == EOF)
                break;
            printf("%c", ch);
            char_count += 1;
        }

        printf(" --- %d\n", char_count);
        char_count = 0;

        if (feof(file))
            break ;

    } while (1);
    fclose(file);
    return 0;
}
