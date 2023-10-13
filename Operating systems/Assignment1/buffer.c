#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_FILE_SIZE 1024
#define MAX_WORD_SIZE 50

void countWords(char *buffer, int start, int end)
{
    int wordCount = 0;

    for (int i = start; i < end; i++)
    {
        if ((buffer[i] == ' ' || buffer[i] == '\n') && (buffer[i - 1] != ' ' && buffer[i - 1] != '\n'))
        {
            wordCount++;
        }
    }

    printf("Child process with PID %d counted %d words.\n", getpid(), wordCount);
    exit(wordCount);
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <num_processes>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int num_processes = atoi(argv[1]);
    if (num_processes <= 0)
    {
        printf("Invalid number of processes. Please provide a positive integer.\n");
        return EXIT_FAILURE;
    }

    FILE *file = fopen("file.txt", "r");
    if (file == NULL)
    {
        perror("Error opening file456");
        return EXIT_FAILURE;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    char *buffer = (char *)malloc(file_size + 1);
    if (buffer == NULL)
    {
        perror("Error allocating memory for buffer");
        fclose(file);
        return EXIT_FAILURE;
    }

    fread(buffer, sizeof(char), file_size, file);
    fclose(file);

    int segment_size = file_size / num_processes;
    int start = 0, end = 0;

    for (int i = 0; i < num_processes; i++)
    {
        if (i == num_processes - 1)
        {
            end = file_size;
        }
        else
        {
            end = start + segment_size;

            while (buffer[end] != ' ' && buffer[end] != '\n')
            {
                end++;
            }
        }

        int pid = fork();

        if (pid == 0)
        {
            countWords(buffer, start, end);
        }
        else if (pid > 0)
        {
            start = end + 1;
        }
        else
        {
            perror("Fork failed");
            free(buffer);
            return EXIT_FAILURE;
        }
    }

    int totalWords = 0;
    int status;
    for (int i = 0; i < num_processes; i++)
    {
        wait(&status);
        totalWords += WEXITSTATUS(status);
    }

    printf("Aggregated word count: %d\n", totalWords);

    free(buffer);
    return EXIT_SUCCESS;
}
