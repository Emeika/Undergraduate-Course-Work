#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

int count_words(FILE *file, long start, long end)
{
    fseek(file, start, SEEK_SET);
    char ch;
    int count = 0;
    while (ftell(file) < end)
    {
        ch = fgetc(file);
        if (ch == ' ' || ch == '\n' || ch == '\t')
            count++;
    }
    return count;
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s filename num_process\n", argv[0]);
        return EXIT_FAILURE;
    }

    char *filename = argv[1];
    int num_processes = atoi(argv[2]);

    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        fprintf(stderr, "Error! Can't open %s\n", filename);
        return EXIT_FAILURE;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    long chunk_size = file_size / num_processes;

    for (int i = 0; i < num_processes; i++)
    {
        pid_t pid = fork();

        if (pid < 0)
        {
            fprintf(stderr, "Fork failed\n");
            return EXIT_FAILURE;
        }
        else if (pid == 0)
        {
            long start = i * chunk_size;
            long end = (i == num_processes - 1) ? file_size : start + chunk_size;

            int count = count_words(file, start, end);

            char output_filename[20];
            sprintf(output_filename, "output%d.txt", i);
            FILE *output_file = fopen(output_filename, "w");
            fprintf(output_file, "%d", count);
            fclose(output_file);

            fclose(file);
            exit(EXIT_SUCCESS); // exit normally
        }
    }

    int total_count = 0;
    for (int i = 0; i < num_processes; i++)
    {
        wait(NULL); // wait for child process to finish

        char output_filename[20];
        sprintf(output_filename, "output%d.txt", i);
        FILE *output_file = fopen(output_filename, "r");
        int count;
        fscanf(output_file, "%d", &count);
        fclose(output_file);

        printf("Child %d: %d words\n", i, count);
        total_count += count;

        remove(output_filename); // delete the file
    }

    printf("Total words: %d\n", total_count);

    fclose(file);

    return EXIT_SUCCESS;
}
