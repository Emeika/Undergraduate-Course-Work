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
    // Open the named pipe (FIFO) for reading
    int fifo_fd = open(FIFO_NAME, O_RDONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // Read a message from the writer
    char buffer[50];
    read(fifo_fd, buffer, sizeof(buffer));

    // Convert the message to uppercase
    for (int i = 0; buffer[i] != '\0'; ++i)
    {
        if (buffer[i] >= 'a' && buffer[i] <= 'z')
        {
            buffer[i] = buffer[i] - 'a' + 'A';
        }
    }

    // Close the FIFO
    close(fifo_fd);

    // Open the named pipe (FIFO) for writing
    fifo_fd = open(FIFO_NAME, O_WRONLY);

    // Send the modified message back to the writer
    write(fifo_fd, buffer, sizeof(buffer));

    // Close the FIFO
    close(fifo_fd);

    return 0;
}