#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {


    char *student_name = argv[1];
    int roll_number = atoi(argv[2]);

    if (roll_number == -1) {
        printf(" Exit\n");
        exit(1);
    }

    FILE *file = fopen("file.txt", "a");

    if (file == NULL) {
        printf("ERROR\n");
        exit(1);
    }

    fprintf(file, "%s %d\n", student_name, roll_number);
    fclose(file);


    file = fopen("file.txt", "r");
    while (fscanf(file, "%s %d", student_name, &roll_number) != EOF) {
        printf("Name: %s\n", student_name);
        printf("Roll Num: %d\n", roll_number);
    }

    fclose(file);
    return 0;
}
