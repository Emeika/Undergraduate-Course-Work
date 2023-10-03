#include <stdio.h>
#include <unistd.h>
#include <wait.h>
int main()
{
    pid_t pid;
    pid = fork();
    if (pid>0) {
        printf("\n In Code section A, my pid is %d\n", getpid());
    }
    else if (pid==0) {
        printf("\n In Code section B, my pid is %d\n", getpid());
        sleep(1);
    }
    return 0;
}

