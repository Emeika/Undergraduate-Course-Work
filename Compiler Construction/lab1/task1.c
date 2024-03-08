//kiran Qaiser 251683919
//Hafsah Shahbaz 251684784

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
    int is_empty_line = 1;
    printf("%d: ", line_count);

    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            if (!is_empty_line) {
                printf(" --- %d\n", char_count);
                char_count = 0;
            } else {
                printf("\n");
            }
            line_count++;
            printf("%d: ", line_count);
            
            is_empty_line = 1;
        } else {
            printf("%c", ch);
            char_count++;
            if (ch != ' ' && ch != '\t' && ch != '\n') {
                is_empty_line = 0;
            }
        }
    }

    if (!is_empty_line) {
        printf(" --- %d\n", char_count);
    }

    fclose(file);

    return 0;
}
