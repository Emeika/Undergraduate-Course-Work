#include <stdio.h>
#include <unistd.h>
#include <wait.h>
int main()
{
    pid_t pid;
    printf("\n Hi \n");
    sleep(1);
    pid = fork();
    printf("\n Hello World!\n");
    return 0;
}



