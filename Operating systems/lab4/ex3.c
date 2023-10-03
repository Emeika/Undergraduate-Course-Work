#include <stdio.h>
#include <unistd.h>
#include <wait.h>
int main()
{
    pid_t pid;
    pid = fork();
    if (pid>0) {
        //wait(NULL); 
        printf("\n I am fine son \n");  // lineA
    }
    else if (pid==0) {
        printf("\n How are u dad ?\n");   // line B
        sleep(1);
    }
    return 0;
}

