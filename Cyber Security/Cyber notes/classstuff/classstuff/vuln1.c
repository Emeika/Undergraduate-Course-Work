#include <stdio.h>
#include <string.h>

void vuln_func(char *input);

int main(int argc, char *argv[])
{
    if (argc > 1)
    {
        vuln_func(argv[1]);
    }
    else
    {
        printf("Usage: %s <input_string>\n", argv[0]);
    }
    return 0;
}

void vuln_func(char *input)
{
    char buffer[256];
    strcpy(buffer, input); // Unsafe function - Vulnerable to buffer overflow
    printf("Buffer content: %s\n", buffer);
}
