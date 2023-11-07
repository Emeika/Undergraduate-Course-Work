// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Date of Lab: 06/11/2023

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdint.h>

void *runner1(void *param);
void *runner2(void *param);
void *runner3(void *param);

int main()
{
    pthread_t tid1, tid2, tid3;

    // Create the first pthread
    printf("thread1 starting \n");
    pthread_create(&tid1, NULL, runner1, (void *)1);

    // Create the second pthread
    printf("thread2 starting \n");
    pthread_create(&tid2, NULL, runner2, (void *)2);

    // Create the third pthread
    printf("thread3 starting \n");
    pthread_create(&tid3, NULL, runner3, (void *)3);

    // Wait for the threads to finish
    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);
    pthread_join(tid3, NULL);

    return 0;
}

void *runner1(void *param)
{
    int threadNumber = (intptr_t)param;
    printf("Thread %d: %ld message1\n", threadNumber, pthread_self());
    pthread_exit(0);
}

void *runner2(void *param)
{
    int threadNumber = (intptr_t)param;
    printf("Thread %d: %ld message2\n", threadNumber, pthread_self());
    pthread_exit(0);
}

void *runner3(void *param)
{
    int threadNumber = (intptr_t)param;
    printf("Thread %d: %ld message3\n", threadNumber, pthread_self());

    pthread_exit(0);
}
