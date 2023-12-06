#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define FIFO_NAME "/tmp/myfifo"

int main()
{
    // Open the named pipe (FIFO) for reading
    int fifo_fd = open(FIFO_NAME, O_RDONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // Read a message from the other program
    char buffer[50];
    read(fifo_fd, buffer, sizeof(buffer));
    printf("Program 2 received message: %s\n", buffer);

    // Close the FIFO
    close(fifo_fd);

    // Remove the named pipe (FIFO)
    unlink(FIFO_NAME);

    return 0;
}
