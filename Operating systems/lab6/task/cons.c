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
    int fd;
    char *ptr;

    // Open the shared memory object
    fd = shm_open(name, O_RDWR, 0666);
    // if (fd == -1)
    // {
    //     perror("shm_open");
    //     return EXIT_FAILURE;
    // }

    // Map the shared memory object
    ptr = (char *)mmap(0, SIZE, PROT_READ, MAP_SHARED, fd, 0);
    // if (ptr == MAP_FAILED)
    // {
    //     perror("mmap");
    //     return EXIT_FAILURE;
    // }

    while (1)
    {
        printf("%s\n", (char *)ptr);

        // if (strcmp(ptr, "exit\n") == 0 || strcmp(ptr, "exit") == 0)
        //     break;

        if (strcmp(ptr, "exit\n") == 0 || strcmp(ptr, "exit") == 0)
            break;

        sleep(3);
    }

    // Unmap and close the shared memory object
    munmap(ptr, SIZE);
    close(fd);

    // Remove the shared memory object
    shm_unlink(name);

    return 0;
}
