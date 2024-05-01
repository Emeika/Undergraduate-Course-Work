#include <stdio.h>
#include "preprocessor.h"

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <inFile>\n", argv[0]);
        return 1;
    }
    removeBlankLines(argv[1]);
    removeComments();
    macroExpansion("../files/withoutCommentsFile.c");


    return 0;
}