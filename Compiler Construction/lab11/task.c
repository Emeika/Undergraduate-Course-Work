#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isTerminal(char symbol)
{
    return (symbol == 'w' || symbol == 'x' || symbol == 'y' || symbol == 'z' || symbol == '$');
}

int parseTable(char s2_nonTerminal, char s1_terminal)
{
    if (s2_nonTerminal == 'A')
    {
        if (s1_terminal == 'y')
            return 1;
        else if (s1_terminal == 'z')
            return 1;
        else if (s1_terminal == '$')
            return 2;
    }
    else if (s2_nonTerminal == 'B')
    {
        if (s1_terminal == 'y')
            return 4;
        else if (s1_terminal == 'z')
            return 3;
    }
    else if (s2_nonTerminal == 'C' && s1_terminal == 'z')
    {
        return 5;
    }
    return -1;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    char *input = argv[1];

    char *s1_input = malloc(10);
    char *s2_production = malloc(10);

    memset(s1_input, '\0', 10);

    memset(s2_production, '\0', 10);

    int top1 = -1, top2 = -1;

    for (int i = strlen(input) - 1; i >= 0; i--)
    {
        s1_input[++top1] = input[i];
    }

    s2_production[++top2] = '$';
    s2_production[++top2] = 'A';

    printf("%-20s%-20s%-10s\n", "Processing Stack", "Input", "Action");
    printf("================================================\n");

    while (1)
    {
        for (int i = strlen(s2_production) - 1; i >= 0; i--)
        {
            putchar(s2_production[i]);
        }

        int space = 20 - (int)strlen(s2_production);
        printf("%-*s", space, "");

        for (int i = strlen(s1_input) - 1; i >= 0; i--)
        {
            putchar(s1_input[i]);
        }
        space = 20 - (int)strlen(s1_input);
        printf("%-*s", space, "");

        if (s1_input[top1] == '$' && s2_production[top2] == '$')
        {
            printf("Accepted\n");
            break;
        }

        if (s1_input[top1] == s2_production[top2])
        {
            printf("pop both stacks\n");
            s1_input[top1] = '\0';
            s2_production[top2] = '\0';
            top1--;
            top2--;
        }
        else if (isTerminal(s1_input[top1]) && (s2_production[top2] == 'A' || s2_production[top2] == 'B' || s2_production[top2] == 'C'))
        {
            int production = parseTable(s2_production[top2], s1_input[top1]);
            printf("%d\n", production);

            if (production == -1)
            {
                printf("Rejected\n");
                break;
            }
            else
            {
                top2--;
                switch (production)
                {
                case 1: // A -> BwA
                    s2_production[++top2] = 'A';
                    s2_production[++top2] = 'w';
                    s2_production[++top2] = 'B';
                    break;
                case 2: // A -> eps
                    s2_production[++top2] = 's';
                    s2_production[++top2] = 'p';
                    s2_production[++top2] = 'e';
                    break;
                case 3: // B -> CxB
                    s2_production[++top2] = 'B';
                    s2_production[++top2] = 'x';
                    s2_production[++top2] = 'C';
                    break;
                case 4: // B -> уC
                    s2_production[++top2] = 'C';
                    s2_production[++top2] = 'y';
                    break;
                case 5: // C -> z
                    s2_production[++top2] = 'z';
                    break;
                }
            }
        }
        else
        {
            s2_production[top2] = '\0';
            s2_production[--top2] = '\0';
            s2_production[--top2] = '\0';
            --top2;
            printf("\n");
        }
    }

    free(s1_input);
    free(s2_production);
    return 0;
}
