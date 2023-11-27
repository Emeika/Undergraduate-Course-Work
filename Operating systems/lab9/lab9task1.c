// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Date of Lab: 11/27/2023

/*
Declare 6 matrices of size NxN each.(e.g., int A[N][N];)
Each k- th(k from 1 to 6) matrix values are calculated according to the following expression :
  3 * i^k - 2 * j^k,   where i, j are the coordinates of a matrix element
The value of each matrix is calculated in a thread, all threads running in parallel.
Each thread writes its matrix to the same text file on disk, after writing "Matrix k."
Implement a mutex to ensure that multiple threads can safely update the result matrix concurrently in the
text file.Only writing to the text file is the critical section.
Test the program and verify your results
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>

#define N 5

void *thread(void *arg);

int matrices[6][N][N];
pthread_mutex_t file_mutex;

int main()
{
    pthread_t tid[6];
    pthread_mutex_init(&file_mutex, NULL);

    for (int i = 1; i <= 6; i++)
    {
        int *arg = malloc(sizeof(*arg));
        *arg = i;
        pthread_create(&tid[i - 1], NULL, thread, arg);
    }

    for (int i = 0; i < 6; i++)
    {
        pthread_join(tid[i], NULL);
    }

    pthread_mutex_destroy(&file_mutex);

    return 0;
}

void *thread(void *arg)
{
    int k = *((int *)arg);
    char filename[20];
    sprintf(filename, "matrix.txt");

    FILE *file = fopen(filename, "a");
    if (file == NULL)
    {
        perror("Error opening file");
        pthread_exit(NULL);
    }

    pthread_mutex_lock(&file_mutex);
    fprintf(file, "Matrix %d:\n", k);
    pthread_mutex_unlock(&file_mutex);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            matrices[k - 1][i][j] = (int)(3 * pow(i, k) - 2 * pow(j, k));

            pthread_mutex_lock(&file_mutex);
            fprintf(file, "%d ", matrices[k - 1][i][j]);
            pthread_mutex_unlock(&file_mutex);
        }

        pthread_mutex_lock(&file_mutex);
        fprintf(file, "\n");
        pthread_mutex_unlock(&file_mutex);
    }

    fclose(file);
    pthread_exit(NULL);
}
