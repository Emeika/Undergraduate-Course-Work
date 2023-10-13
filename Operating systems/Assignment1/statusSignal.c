#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

// exit status signal can only hold max 250 word count

int count_words(FILE *file, long start, long end)
{
    fseek(file, start, SEEK_SET); // Move the file pointer to the specified starting position
    char ch;
    int count = 0;

    // Loop until the current file position is less than the specified ending position
    while (ftell(file) < end)
    {
        ch = fgetc(file);                          // Read a character from the file
        if (ch == ' ' || ch == '\n' || ch == '\t') // encountered the end of a word so ++count
            count++;
    }
    return count;
}

int main(int argc, char *argv[])
{
    if (argc != 3) // if both filename and process count not given as arguments
    {
        fprintf(stderr, "Usage: %s filename num_process\n", argv[0]);
        return EXIT_FAILURE;
    }

    char *file = argv[1];
    int num_processes = atoi(argv[2]);

    if (num_processes < 0) // if num of processes is negative
    {
        fprintf(stderr, "Invalid number of process\n");
        return EXIT_FAILURE;
    }

    FILE *fptr = fopen(file, "r");
    if (fptr == NULL) // if file doesn't exist
    {
        fprintf(stderr, "Error! Can't open %s\n", file);
        return EXIT_FAILURE;
    }

    fseek(fptr, 0, SEEK_END);     // moves the file pointer to 0 positions away from the end of the file,
    long file_size = ftell(fptr); // ftell() to get current position of fptr to find size of the file in bytes.
    fseek(fptr, 0, SEEK_SET);     // reset the file pointer back to the start of the file at 0 position

    long chunk_size = file_size / num_processes; // Calculate chunk size for each child process

    // Create child processes
    for (int i = 0; i < num_processes; i++)
    {
        pid_t pid = fork();
        if (pid < 0)
        {
            fprintf(stderr, "Fork failed! Can't create child process\n");
            return EXIT_FAILURE;
        }

        else if (pid == 0)
        {
            // Calculate the starting and ending positions for each chunk of the file
            long start = i * chunk_size; // Starting position
            // If 'i' is the last child process, set 'end' to 'file_size'
            // Otherwise, set 'end' to 'start + chunk_size'
            long end = (i == num_processes - 1) ? file_size : start + chunk_size; // Ending position

            int count = count_words(fptr, start, end);
            fclose(fptr);
            exit(count); // exit child process & pass the count as the exit status
        }
    }
    int total_count = 0;
    for (int i = 0; i < num_processes; i++)
    {
        int status; // holds the exit status of a child process

        // Wait for a child process to terminate and retrieve its exit status
        // The address of `status` is passed to store the exit status of the child process, & Store the terminated child process ID in `child_pid`
        pid_t child_pid = wait(&status);

        if (WIFEXITED(status)) // if the child process terminated normally (without signals)
        {
            int count = WEXITSTATUS(status); // exit status(word count) provided by the child process
            printf("Child %d with pid %d: %d words\n", i + 1, child_pid, count);
            total_count += count;
        }
    }
    printf("Total words: %d\n", total_count);

    fclose(fptr);
    return EXIT_SUCCESS;
}