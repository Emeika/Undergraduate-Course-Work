#include <stdio.h>
#include <unistd.h>
#include <wait.h>
int main()
{
    pid_t pid1, pid2;
    pid1 = fork();
    if (pid1>0) {
        wait(NULL); 
        printf("Parent: My pid= %d\n", getpid());
        printf("Parent: My parent's pid= %d\n", getppid());
        printf("Parent: My child's pid= %d\n", pid1);
    }
    else if (pid1==0) {
        printf("Child: My pid= %d\n", getpid());
        printf("Child: My parent's pid= %d\n", getppid());
        pid2=fork();
        if (pid2==0) {
            printf("Grand child: My pid= %d\n", getpid());
            printf("Grand child: My parent's pid= %d\n", getppid());
        }
        else if(pid2>0) 
            wait(NULL);
    }
    return 0;
}

