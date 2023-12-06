// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Due Date: 04/10/2023

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define FIFO_NAME "/tmp/myfifo"

int main()
{
    // Create the named pipe (FIFO) if it doesn't exist
    mkfifo(FIFO_NAME, 0666);

    int fifo_fd = open(FIFO_NAME, O_WRONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // Send a lowercase message to the reader
    char message[] = "hello from writer!";
    write(fifo_fd, message, sizeof(message));

    // Close the FIFO
    close(fifo_fd);

    // Open the named pipe (FIFO) for reading
    fifo_fd = open(FIFO_NAME, O_RDONLY);

    // Read the modified message from the reader
    char modifiedMessage[50];
    read(fifo_fd, modifiedMessage, sizeof(modifiedMessage));

    // Print the modified message
    printf("Program 1 received message: %s\n", modifiedMessage);

    // Close the FIFO
    close(fifo_fd);

    // Remove the named pipe (FIFO)
    unlink(FIFO_NAME);

    return 0;
}