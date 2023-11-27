#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

pthread_t tid[2];
int enable = 1;
pthread_mutex_t lock;

void *thread1(void *arg);
void *thread2(void *arg);

int main(void)
{
    printf("Enter 1 to enable Mutex, 0 to disable: ");
    scanf("%d", &enable);
    if (pthread_mutex_init(&lock, NULL) != 0)
    {
        printf("\n mutex init has failed\n");
        return 1;
    }

    pthread_create(&(tid[0]), NULL, &thread1, NULL);
    pthread_create(&(tid[1]), NULL, &thread2, NULL);

    pthread_join(tid[0], NULL); // wait for thread to completely execute.
    pthread_join(tid[1], NULL);
    pthread_mutex_destroy(&lock);

    return 0;
}

void *thread1(void *arg)
{
    if (enable)
        pthread_mutex_lock(&lock);
    for (int i = 0; i < 200; i++)
    {
        printf("-");
        // fflush(stdout); // refresh console for printing.
        for (int j = 0; j < 0x3FFFFF; j++)
            ; // keep the thread busy in CPU
    }
    if (enable)
        pthread_mutex_unlock(&lock);
}

void *thread2(void *arg)
{
    if (enable)
        pthread_mutex_lock(&lock);
    for (int i = 0; i < 200; i++)
    {
        printf("x");
        // fflush(stdout);
        for (int j = 0; j < 0x3FFFFF; j++)
            ;
    }
    if (enable)
        pthread_mutex_unlock(&lock);
}
