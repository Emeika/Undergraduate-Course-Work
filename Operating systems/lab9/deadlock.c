#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

void *thread1(void *arg);
void *thread2(void *arg);
void *deadlock_detect(void *arg); // thread3

pthread_mutex_t lock1; // lock1 represents a resource e.g. "file on disk"
pthread_mutex_t lock2; // lock2 represents a resource e.g. "USB port"
int lock1th1 = 0, lock2th2 = 0;

int main()
{
    pthread_t tid[3];
    pthread_mutex_init(&lock1, NULL);
    pthread_mutex_init(&lock2, NULL);

    pthread_create(&tid[0], NULL, &thread1, NULL);
    pthread_create(&tid[1], NULL, &thread2, NULL);
    pthread_create(&tid[2], NULL, &deadlock_detect, NULL);

    for (int i = 0; i < 2; i++)
        pthread_join(tid[i], NULL);
    pthread_mutex_destroy(&lock1);
    pthread_mutex_destroy(&lock2);

    return 0;
}

void *thread1(void *arg)
{
    while (1)
    {
        pthread_mutex_lock(&lock1);
        lock1th1 = 1;
        for (int i = 0; i < 0xFFF; i++)
            ; // Add delay between resource requests
        pthread_mutex_lock(&lock2);
        lock1th1 = 0;
        for (int i = 0; i < 0xFFFFFF; i++)
            ;        // thread busy doing some work
        printf("1"); // prints when thread 1 is done
        pthread_mutex_unlock(&lock2);
        pthread_mutex_unlock(&lock1);
    }
}

void *thread2(void *arg)
{
    while (1)
    {
        pthread_mutex_lock(&lock2);
        lock2th2 = 1;
        for (int i = 0; i < 0xFFF; i++)
            ; // Add delay between resource requests
        pthread_mutex_lock(&lock1);
        lock2th2 = 0;

        for (int i = 0; i < 0xFFFFFF; i++)
            ;        // thread busy doing some work
        printf("2"); // prints when thread 2 is done
        pthread_mutex_unlock(&lock1);
        pthread_mutex_unlock(&lock2);
    }
}

void *deadlock_detect(void *arg)
{
    while (1)
    {
        fflush(stdout);
        for (int i = 0; i < 0xFFF; i++)
            ; // delay between iterations
        if (lock1th1 && lock2th2)
        {
            pthread_mutex_destroy(&lock1);
            pthread_mutex_destroy(&lock2);
            break;
        }
    }
    printf("! Deadlock Occurred ! (Ctrl+C to terminate)\n");
}
