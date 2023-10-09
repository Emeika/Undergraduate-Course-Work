#include<sys/types.h>
#include<sys/types.h>
#include<dirent.h>
#include<stdio.h>
int main (int c, char* arg []) { 
    DIR *d;
    struct dirent *r;
    int i=0;
    d=opendir (arg [1]);
    printf("\n\t NAME OF ITEM \n"); while ((r=readdir (d)) != NULL) 
    while ((r=readdir(d) ) != NULL) {
        printf("\t%s \n", r->d_name);
        i=i+1;
        
    }

    
    printf("\n TOTAL NUMBER OF ITEMS IN THAT DIRECTORY ARE %d \n", i);
    return 0;
}



  file = fopen("student_records.txt", "r");









    printf("\nContents of the file:\n");
    char line[100];
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    fclose(file);
