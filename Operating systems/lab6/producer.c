// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Due Date: 16/10/2023
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
    const char *message_0 = "Hello";
    const char *message_1 = "World!";
    int fd;
    char *ptr;
    int *ptr1;

    fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    ftruncate(fd, SIZE);
    ptr = (char *)mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    ptr1 = (int *)(ptr + SIZE - sizeof(int));

    while (1)
    {
        printf("Enter a message (or 'exit' to quit): ");
        char input[100];
        scanf("%s", input);

        if (strcmp(input, "exit") == 0)
        {
            *ptr1 = 1;
            break;
        }
        else
        {
            sprintf(ptr, "%s", input);
            ptr += strlen(input);
        }
    }

    shm_unlink(name);
    return 0;
}