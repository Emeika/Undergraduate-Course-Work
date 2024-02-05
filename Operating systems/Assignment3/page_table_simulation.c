// Course Code: 301-B
// Name: Hafsah Shahbaz
// Roll Number: 251684784

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct PageTableEntry
{
    int pageNumber;
    int frameNumber;
    // You can add more data fields as needed
};

#define MAX_ENTRIES 5
#define NUM_ACCESS 20 // Number of virtual page accesses

void initializePageTable(struct PageTableEntry pageTable[], int numEntries)
{
    for (int i = 0; i < numEntries; i++)
    {
        pageTable[i].pageNumber = -1;
        pageTable[i].frameNumber = -1;
        // Initialize other data fields as needed
    }
}

int pageTableLookup(struct PageTableEntry pageTable[], int numEntries, int virtualPageNumber)
{
    for (int i = 0; i < numEntries; i++)
    {
        if (pageTable[i].pageNumber == virtualPageNumber)
        {
            return i;
        }
    }
    return -1;
}

void displayPageTable(struct PageTableEntry pageTable[], int numEntries)
{
    printf("Page Table:\n");
    printf("Page Number\tFrame Number\n");
    for (int i = 0; i < numEntries; i++)
    {
        printf("%d\t\t%d\n", pageTable[i].pageNumber, pageTable[i].frameNumber);
    }
    printf("\n");
}

int main()
{
    // Create a page table with a specified number of entries
    struct PageTableEntry pageTable[MAX_ENTRIES];
    initializePageTable(pageTable, MAX_ENTRIES);

    // Display the initial contents of the page table
    displayPageTable(pageTable, MAX_ENTRIES);

    // Seed the random number generator
    srand(time(NULL));

    int pageFaults = 0;
    int pageReplacements = 0;

    // Generate a sequence of virtual page accesses
    printf("Virtual Page Access Sequence:\n");
    for (int i = 0; i < NUM_ACCESS; i++)
    {
        int virtualPageToAccess = rand() % MAX_ENTRIES;
        printf("%d ", virtualPageToAccess);

        // Perform a page table lookup
        int index = pageTableLookup(pageTable, MAX_ENTRIES, virtualPageToAccess);

        // Simulate page fault if the virtual page is not present
        if (index == -1)
        {
            pageFaults++;

            // Find the first available frame using FIFO
            int freeFrame = i % MAX_ENTRIES;

            // Check if the frame is already occupied
            if (pageTable[freeFrame].pageNumber != -1)
            {
                pageReplacements++;
                printf("(Page Replacement) ");
            }

            // Simulate demand paging by loading the missing page into memory
            pageTable[freeFrame].pageNumber = virtualPageToAccess;
            pageTable[freeFrame].frameNumber = freeFrame;

            // Print information about the page being loaded
            printf("Loading virtual page %d into frame %d\n", virtualPageToAccess, freeFrame);
        }
    }
    printf("\n");

    // Display the final contents of the page table
    displayPageTable(pageTable, MAX_ENTRIES);

    // Display page fault and page replacement statistics
    printf("Page Faults: %d\n", pageFaults);
    printf("Page Replacements: %d\n", pageReplacements);

    return 0;
}
