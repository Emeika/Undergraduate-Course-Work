#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void *runner(void *param);

int main()
{
    pthread_t tid;
    printf("thread starting \n");
    pthread_create(&tid, NULL, runner, NULL);

    // pthread_join(tid, NULL);

    for (int i = 0; i < 10000; i++)
    {
        printf(".");
    }

    return 0;
}

void *runner(void *param)
{
    for (int i = 0; i < 10000; i++)
    {
        printf("/");
    }
    pthread_exit(0);
}