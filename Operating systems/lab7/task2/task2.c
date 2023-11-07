// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Date of Lab: 06/11/2023

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdint.h>

void *factorial(void *param);

int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int r = atoi(argv[2]);
    pthread_t tid1, tid2, tid3;
    int n_r = n - r;

    // Create the pthreads
    pthread_create(&tid1, NULL, factorial, &n);
    pthread_create(&tid2, NULL, factorial, &r);
    pthread_create(&tid3, NULL, factorial, &n_r);

    // Wait for the threads to finish
    void *res1, *res2, *res3;
    pthread_join(tid1, &res1);
    pthread_join(tid2, &res2);
    pthread_join(tid3, &res3);

    // Calculate nCr
    int nCr = (intptr_t)res1 / ((intptr_t)res2 * (intptr_t)res3);
    printf("nCr = %d\n", nCr);

    return 0;
}

void *factorial(void *param)
{
    int n = *(int *)param;
    int fact = 1;
    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    printf("%d! = %d\n", n, fact);
    return (void *)(intptr_t)fact;
}
