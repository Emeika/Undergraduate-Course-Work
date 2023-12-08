// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784
// Due Date: 12/10/2023

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#define MAX_PATH_LEN 256
#define MAX_BUFFER_LEN 1024
#define MAX_PROCESSES 10

// Function to read and display total and free memory
void displayMemoryInfo()
{
    FILE *memInfo = fopen("/proc/meminfo", "r");
    if (memInfo != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        while (fgets(buffer, sizeof(buffer), memInfo) != NULL)
        {
            if (strncmp(buffer, "MemTotal:", 9) == 0 || strncmp(buffer, "MemFree:", 8) == 0)
            {
                printf("%s", buffer);
            }
        }
        fclose(memInfo);
    }
    else
    {
        perror("Error opening /proc/meminfo");
    }
}

// Function to read and display CPU usage
void displayCpuUsage()
{
    FILE *statFile = fopen("/proc/stat", "r");
    if (statFile != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        if (fgets(buffer, sizeof(buffer), statFile) != NULL)
        {
            if (strncmp(buffer, "cpu ", 4) == 0)
            {
                unsigned long long user, nice, system, idle;
                sscanf(buffer + 4, "%llu %llu %llu %llu", &user, &nice, &system, &idle);

                unsigned long long totalCpuTime = user + nice + system + idle;
                unsigned long long idleTime = idle;

                double cpuUsage = ((totalCpuTime - idleTime) * 100.0) / totalCpuTime;
                printf("CPU Usage: %.2f%%\n", cpuUsage);
            }
        }
        fclose(statFile);
    }
    else
    {
        perror("Error opening /proc/stat");
    }
}

// Function to read and display disk usage
void displayDiskUsage()
{
    FILE *df = popen("df -h /", "r");
    if (df != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        if (fgets(buffer, sizeof(buffer), df) != NULL)
        {
            printf("Disk Usage: %s", buffer);
        }
        pclose(df);
    }
    else
    {
        perror("Error running df command");
    }
}

// Function to display the top N processes
void displayTopProcesses(int topN)
{
    printf("\n");
    printf("%-4s%-13s%-5s%-5s%-5s%-6s%-7s%-8s%-12s%-20s\n", "Rank", "USER", "PID", "%CPU", "%MEM", "VSZ", "RSS", "TTY", "STAT", "COMMAND");

    // Run 'ps' command to get the top processes
    char psCommand[MAX_BUFFER_LEN];
    snprintf(psCommand, sizeof(psCommand), "ps aux --sort=-%%cpu,%%mem -ww | head -n+%d", topN + 6);

    FILE *ps = popen(psCommand, "r");
    if (ps != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        int counter = 1; // Counter for numbering processes
        while (fgets(buffer, sizeof(buffer), ps) != NULL)
        {
            if (counter > 5) // Skip the header lines
            {
                // Extract and print relevant information with proper formatting
                char user[16], pid[8], cpu[8], mem[8], vsz[8], rss[8], tty[8], stat[8], command[MAX_BUFFER_LEN]; // command[159] for beter formatting

                // Extract information from the current line
                sscanf(buffer, "%s%s%s%s%9s%s%s%s", user, pid, cpu, mem, vsz, rss, tty, stat);

                // Read the entire command line into the 'command' variable
                fgets(command, sizeof(command), ps);

                // Print the information
                printf("%-4d%-20s", counter - 5, command);
            }
            counter++;
        }

        pclose(ps);
    }
    else
    {
        perror("Error running ps command");
    }
}

int main()
{
    int updateInterval = 5; // seconds
    int topNProcesses;

    // Allow the user to specify the number of processes to display
    printf("Enter the number of top processes to display: ");
    scanf("%d", &topNProcesses);

    if (topNProcesses <= 0 || topNProcesses > MAX_PROCESSES)
    {
        fprintf(stderr, "Invalid number of processes. Please enter a value between 1 and %d\n", MAX_PROCESSES);
        return EXIT_FAILURE;
    }

    while (1)
    {
        // Clear the terminal
        system("clear");

        // Display system information
        printf("System Information:\n");
        displayMemoryInfo();
        displayCpuUsage();
        displayDiskUsage();
        displayTopProcesses(topNProcesses);

        // Sleep for the specified update interval
        sleep(updateInterval);
    }

    return 0;
}