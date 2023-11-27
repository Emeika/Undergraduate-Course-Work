// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Due Date: 13/11/2023

#include <stdio.h>
#include <string.h>

void main()
{
    float avgwt, avgtt;
    char pname[20][10], c[20][10];
    int wt[20], tt[20], bt[20], rt[20];
    int at[20], t, q, i, n_rr, n_fcfs, sum_rr = 0, sbt_rr = 0, ttime_rr, j_rr, ss_rr = 0;
    int otq, rrq;

    printf("\n\n Enter the Outer Time Quantum (OTQ): ");
    scanf("%d", &otq);
    printf("\n\n Enter the Time Quantum (Q) for RR queue: ");
    scanf("%d", &rrq);

    // Total number of processes (RR + FCFS)
    int n_total;

    printf("\n\n Enter the number of processes for RR queue: ");
    scanf("%d", &n_rr);

    printf("\n\n Enter the following information about each process in RR queue");

    for (i = 0; i < n_rr; i++)
    {
        printf("\n\n For Process p[%d]:\n", i);
        printf("\n\n  NAME : ");
        scanf("%s", pname[i]);
        printf("\n\n  BURST TIME : ");
        scanf("%d", &bt[i]);
        printf("\n\n  ARRIVAL TIME : ");
        scanf("%d", &at[i]);
        rt[i] = bt[i];
    }

    printf("\n\n Enter the number of processes for FCFS queue: ");
    scanf("%d", &n_fcfs);

    printf("\n\n Enter the following information about each process in FCFS queue");

    for (i = 0; i < n_fcfs; i++)
    {
        printf("\n\n For Process p[%d]:\n", i + n_rr); // Adjust index for FCFS processes
        printf("\n\n  NAME : ");
        scanf("%s", pname[i + n_rr]); // Adjust index for FCFS processes
        printf("\n\n  BURST TIME : ");
        scanf("%d", &bt[i + n_rr]); // Adjust index for FCFS processes
        printf("\n\n  ARRIVAL TIME : ");
        scanf("%d", &at[i + n_rr]); // Adjust index for FCFS processes
    }

    // Combine RR and FCFS processes
    n_total = n_rr + n_fcfs;

    // Outer Loop treating RR and FCFS as processes
    for (i = 0; i < n_total; i++)
    {
        if (i < n_rr)
        {
            // Round Robin (RR) Logic
            ttime_rr = 0;
            j_rr = i;

            while (j_rr < n_rr)
            {
                if (at[j_rr] <= ttime_rr && rt[j_rr] > 0)
                {
                    printf("|\t%s\t", pname[j_rr]);
                    wt[j_rr] = ttime_rr;
                    if (rt[j_rr] <= rrq)
                    {
                        ttime_rr += rt[j_rr];
                        rt[j_rr] = 0;
                        tt[j_rr] = wt[j_rr] + bt[j_rr];
                        ss_rr += tt[j_rr];
                    }
                    else
                    {
                        ttime_rr += rrq;
                        rt[j_rr] -= rrq;
                    }
                }
                else
                {
                    printf("|\t\t");       // Adjust spacing for FCFS
                    ttime_rr += otq - rrq; // Allocate time for FCFS
                }
                j_rr++;
            }
        }
        else
        {
            // First Come First Serve (FCFS) Logic
            wt[i] = wt[i - 1] + bt[i - 1];
            sum_rr = sum_rr + (wt[i] - at[i]);
            sbt_rr = sbt_rr + (wt[i] + bt[i] - at[i]);
            tt[i] = wt[i] + bt[i];
            ss_rr = ss_rr + bt[i];
        }
    }

    avgwt = (float)sum_rr / n_total;
    avgtt = (float)sbt_rr / n_total;
    printf("\n\n Average waiting time (Combined) = %f", avgwt);
    printf("\n\n Average turn-around time (Combined) = %f", avgtt);

    printf("\n\n GANTT CHART (Combined)\n");

    for (i = 0; i < n_total; i++)
        printf("|\t%s\t", pname[i]);

    printf("\n");

    for (i = 0; i < n_total; i++)
        printf("%d\t\t", wt[i]);

    printf("%d\n", ss_rr);
    printf("\n");
}
