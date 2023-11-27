#include <stdio.h>
#include <string.h>

void main()
{
    float avgwt, avgtt;
    char pname[20][10], c[20][10], gantt[100];
    int wt[20], tt[20], bt[20], at[20], q1, q2, n, i, j, sum = 0, sbt = 0, ttime, ss = 0;

    printf("\nEnter the number of processes: ");
    scanf("%d", &n);

    printf("\nEnter the following information about each process\n");

    for (i = 0; i < n; i++)
    {
        printf("\nFor Process p[%d]:\n", i);
        printf("\nNAME: ");
        scanf("%s", pname[i]);
        printf("\nBURST TIME: ");
        scanf("%d", &bt[i]);
        printf("\nARRIVAL TIME: ");
        scanf("%d", &at[i]);
    }

    printf("\nEnter Outer Time Quantum (OTQ): ");
    scanf("%d", &q1);

    printf("\nEnter Quantum for RR queue (Q): ");
    scanf("%d", &q2);

    // FCFS Scheduling
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (at[i] > at[j])
            {
                int t = at[i];
                at[i] = at[j];
                at[j] = t;

                int temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;

                strcpy(c[i], pname[i]);
                strcpy(pname[i], pname[j]);
                strcpy(pname[j], c[i]);
            }
        }
    }

    wt[0] = 0;
    for (i = 0; i < n; i++)
    {
        wt[i + 1] = wt[i] + bt[i];
        sum = sum + (wt[i] - at[i]);
        sbt = sbt + (wt[i + 1] - at[i]);
        tt[i] = wt[i] + bt[i];
        ss = ss + bt[i];
    }

    avgwt = (float)sum / n;
    avgtt = (float)sbt / n;
    printf("\nAverage waiting time for FCFS = %f", avgwt);
    printf("\nAverage turn-around time for FCFS = %f", avgtt);
    printf("\nGANTT CHART for FCFS\n");

    for (i = 0; i < n; i++)
    {
        printf("|\t%s\t", pname[i]);
    }

    printf("\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t\t", wt[i]);
    }

    printf("%d\n", ss);
    printf("\n");

    // Round Robin Scheduling
    int temp_bt[20];
    for (i = 0; i < n; i++)
    {
        temp_bt[i] = bt[i];
    }

    int time = 0;
    while (1)
    {
        int flag = 0;
        for (i = 0; i < n; i++)
        {
            if (temp_bt[i] > 0)
            {
                flag = 1;

                if (temp_bt[i] > q2)
                {
                    sprintf(gantt, "%s|%d-%d|", gantt, time, time + q2);
                    time += q2;
                    temp_bt[i] -= q2;
                }
                else
                {
                    sprintf(gantt, "%s|%d-%d|", gantt, time, time + temp_bt[i]);
                    time += temp_bt[i];
                    wt[i] = time - bt[i] - at[i];
                    temp_bt[i] = 0;
                }
            }
        }

        if (flag == 0)
        {
            break;
        }
    }

    printf("\nGANTT CHART for Round Robin\n%s\n", gantt);

    // Calculate average waiting time and turn-around time for RR
    sum = 0;
    sbt = 0;
    ss = 0;

    for (i = 0; i < n; i++)
    {
        tt[i] = wt[i] + bt[i];
        sum += wt[i];
        sbt += tt[i];
        ss += bt[i];
    }

    avgwt = (float)sum / n;
    avgtt = (float)sbt / n;
    printf("\nAverage waiting time for RR = %f", avgwt);
    printf("\nAverage turn-around time for RR = %f\n", avgtt);
}
