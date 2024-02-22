#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    char ch;
    int line_count = 1;
    int char_count = 0;

    printf("%d: ", line_count);
    while ((ch = fgetc(file)) != EOF) {
        // Print character
        printf("%c", ch);
        char_count++;

        // If a newline character is encountered, print character count
        if (ch == '\n' && ch != '\0') {
            printf(" --- %d\n", char_count - 1); // Subtract 1 to exclude the newline character
            char_count = 0;
            line_count++;
            if (ch != '\n') {
                printf("%d: ", line_count); // Increment line_count by 1 since we're printing the next line
            }
        }
    }

    fclose(file);

    return 0;
}
