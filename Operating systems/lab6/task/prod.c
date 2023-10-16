#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    const int SIZE = 4096;
    const char *name = "OS";
    char *message = "as\n";
    int fd;
    char *ptr;

    // Open the shared memory object
    fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    ftruncate(fd, SIZE); // Set the size

    // Map the shared memory object
    ptr = (char *)mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

    while (1)
    {
        printf("Enter a line ('exit' to quit):\n");
        fgets(ptr, SIZE, stdin);

        // Check if the user wants to exit
        if (strcmp(ptr, "exit\n") == 0)
            break;

        // Move the pointer to the end of the written message
        ptr += strlen(ptr);
        sleep(1); // Sleep to simulate some processing time
    }

    // Unmap and close the shared memory object
    munmap(ptr, SIZE);
    close(fd);

    return 0;
}
