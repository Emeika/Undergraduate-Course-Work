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

    // Send a message to the other program
    char message[] = "Hello from Program 1!";
    write(fifo_fd, message, sizeof(message));

    // Close the FIFO
    close(fifo_fd);

    return 0;
}
