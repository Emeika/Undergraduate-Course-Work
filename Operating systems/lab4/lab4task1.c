//Course Code: 301-B
//Name: Hafsah Shahbaz
//Roll Number: 251684784
//Date of Lab: 02/10/2023

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>
int main(int argc, char *argv[])
{
    int child = atoi(argv[1]);
    int grandchild = atoi(argv[2]);
    pid_t pid1, pid2;
    pid1 = fork();
    for (int i =0; i < child; i++) {
        if (pid1>0) {
        wait(NULL); 
        printf("\nI am at level 1\n");
        printf("Parent: My pid= %d\n", getpid());
        printf("Parent: My parent's pid= %d\n", getppid());
        printf("Parent: My child's pid= %d\n", pid1);
        
        }
        else if (pid1==0) {
            printf("\nI am at level 2\n");
            printf("Child: My pid= %d\n", getpid());
            printf("Child: My parent's pid= %d\n", getppid());
            
            pid2=fork();
            for (int j = 0; j< grandchild; j++) {
                if (pid2==0) {
                    printf("\nI am at level 3\n");
                    printf("Grand child: My pid= %d\n", getpid());
                    printf("Grand child: My parent's pid= %d\n", getppid());
                    
                }
                else if(pid2>0) 
                    wait(NULL);
            }
            
        }
    }
    
    return 0;
}

