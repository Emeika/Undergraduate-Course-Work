#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void args_check(int argc, char **argv);
int validate_number(char **argv);
void disp_file_on_console(FILE *fp);
void file_decoder(FILE *fp, char **argv);

void args_check(int argc, char **argv) {
    if (argc < 3) {
        printf("Usage: %s <filename><1-5>\n", argv[0]);
        exit(1);
    }
}

int validate_number(char **argv) {
    int num = atoi(argv[2]);
    if (num < 1 || num > 5) {
        printf("Usage: %s %s <1-5>\n", argv[0], argv[1]);
        printf("Invalid input: %s is not a valid number.\n", argv[2]);
        exit(1);
    }
    return num;
}

void disp_file_on_console(FILE *fp) {
    int max = 100;
    char buf[max];

    while (fgets(buf, max, fp) != NULL) {
        for (int i = 0; buf[i] != '\0' && buf[i] != '\n'; i++) {
            putchar(buf[i]);
        }
        putchar('\n');
    }
}

void file_decoder(FILE *fp, char **argv) {
    int max = 100;
    char buf[max];
    int shift = atoi(argv[2]);

    while (fgets(buf, max, fp) != NULL) {
        for (int i = 0; buf[i] != '\0' && buf[i] != '\n'; i++) {
            char c = buf[i];

            if (isspace(c) || c == ',' || c == ':' || c == ';' || c=='?' || c=='!'|| c =='.') {
                putchar(c);
            } else {
                char shifted_char = 'a' + (c - 'a' + shift) % 26;
                putchar(shifted_char);
            }
        }
        putchar('\n');
    }
}

int main(int argc, char **argv) {
    args_check(argc, argv);

    int num = validate_number(argv);

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("Error opening file %s\n", argv[1]);
        exit(1);
    }

    printf("The Input File:\n");
    disp_file_on_console(fp);
    fclose(fp);

    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("Error opening file %s\n", argv[1]);
        exit(1);
    }
    printf("The Output File:\n");
    file_decoder(fp, argv);

    fclose(fp);

    return 0;
}
