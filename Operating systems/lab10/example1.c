#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int pipe_fd[2]; // File descriptors for the pipe:
                    //   pipe_fd[0] for reading, pipe_fd[1] for writing
    pid_t child_pid;

    // Create a pipe
    if (pipe(pipe_fd) == -1)
    {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    // Create a child process
    if ((child_pid = fork()) == -1)
    {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0)
    { // Child process

        close(pipe_fd[0]); // Close the read end, as the child will write
                           //--------------------------------LINE A----------------------
        // Introduce a delay of around 5 seconds using a loop
        for (int i = 0; i < 0xfffff; i++)
        {
        }

        // Write a message to the pipe
        char message[] = "Hello from the child!";
        write(pipe_fd[1], message, sizeof(message));

        close(pipe_fd[1]); // Close the write end after writing
        exit(EXIT_SUCCESS);
    }
    else
    { // Parent process

        close(pipe_fd[1]); // Close the write end, as the parent will read
                           //--------------------------------LINE B----------------------
        // Print a message before reading
        printf("Parent ready to receive the message\n");

        // Read from the pipe
        char buffer[50];
        read(pipe_fd[0], buffer, sizeof(buffer));

        printf("Parent received message: %s\n", buffer);
        close(pipe_fd[0]); // Close the read end after reading

        // Wait for the child to finish
        wait(NULL);

        exit(EXIT_SUCCESS);
    }
}
