#ifndef PREPROCESSOR_H
#define PREPROCESSOR_H

#define MAX_LINE_LENGTH 2024
#define MAX_LINES 2024
#define MAX_MACROS 10

typedef struct {
    char name[MAX_LINE_LENGTH];
    char value[MAX_LINE_LENGTH];
} Macro;

void removeBlankLines(const char *inputFile);
void removeComments();
void macroExpansion(const char *inputFile);


#endif