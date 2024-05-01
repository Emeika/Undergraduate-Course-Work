#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <string>\n", argv[0]);
        return 1;
    }

    char *input_str = argv[1];

    // check if string ends with $
    if (input_str[strlen(input_str) - 1] != '$')
    {
        printf("String does not end with $\nExiting...\n");
        return 1;
    }

    printf("Input String is: %s\n", input_str);
    printf("State transitions are shown below:\n");

    char *current_state = "q0";
    int total_char = strlen(input_str);
    int i = -1;     // iterator
    int accept = 0; // flag to indicate if string is accepted or not (-1 for unknown character)

    // start of the state machine
    goto q0;

q0:
    current_state = "q0";
    i += 1;

    if (input_str[i] == 'a')
    {
        printf("Received %c on state %s ---- Moving to state q1\n", input_str[i], current_state);
        goto q1;
    }
    else if (input_str[i] == 'b')
    {
        printf("Received %c on state %s ---- Moving to state q3\n", input_str[i], current_state);
        goto q3;
    }
    else if (input_str[i] == '$')
    {
        accept = 0;
        goto finish;
    }
    else
    {
        printf("Received unknown character %c on state %s\n", input_str[i], current_state);
        accept = -1;
        goto finish;
    }

q1:
    current_state = "q1";
    i += 1;

    if (input_str[i] == 'a')
    {
        printf("Received %c on state %s ---- Moving to state q2\n", input_str[i], current_state);
        goto q2;
    }
    else if (input_str[i] == 'b')
    {
        printf("Received %c on state %s ---- Moving to state q3\n", input_str[i], current_state);
        goto q3;
    }
    else if (input_str[i] == '$')
    {
        accept = 0;
        goto finish;
    }
    else
    {
        printf("Received unknown character %c on state %s\n", input_str[i], current_state);
        accept = -1;
        goto finish;
    }

q2:
    current_state = "q2";
    i += 1;

    if (input_str[i] == 'a')
    {
        printf("Received %c on state %s ---- Moving to state q2\n", input_str[i], current_state);
        goto q2;
    }
    else if (input_str[i] == 'b')
    {
        printf("Received %c on state %s ---- Moving to state q3\n", input_str[i], current_state);
        goto q3;
    }
    else if (input_str[i] == '$')
    {
        accept = 1;
        goto finish;
    }
    else
    {
        printf("Received unknown character %c on state %s\n", input_str[i], current_state);
        accept = -1;
        goto finish;
    }

q3:
    current_state = "q3";
    i += 1;

    if (input_str[i] == 'a')
    {
        printf("Received %c on state %s ---- Moving to state q1\n", input_str[i], current_state);
        goto q1;
    }
    else if (input_str[i] == 'b')
    {
        printf("Received %c on state %s ---- Moving to state q4\n", input_str[i], current_state);
        goto q4;
    }
    else if (input_str[i] == '$')
    {
        accept = 0;
        goto finish;
    }
    else
    {
        printf("Received unknown character %c on state %s\n", input_str[i], current_state);
        accept = -1;
        goto finish;
    }

q4:
    current_state = "q4";
    i += 1;

    if (input_str[i] == 'a')
    {
        printf("Received %c on state %s ---- Moving to state q1\n", input_str[i], current_state);
        goto q1;
    }
    else if (input_str[i] == 'b')
    {
        printf("Received %c on state %s ---- Moving to state q4\n", input_str[i], current_state);
        goto q4;
    }
    else if (input_str[i] == '$')
    {
        accept = 1;
        goto finish;
    }
    else
    {
        printf("Received unknown character %c on state %s\n", input_str[i], current_state);
        accept = -1;
        goto finish;
    }

finish:
    if (accept == -1)
    {
        printf("Terminating the process...\n");
        return 1;
    }

    printf("End of string.\n");

    if (accept == 0)
    {
        printf("String rejected.\n");
        return 1;
    }
    else if (accept == 1)
    {
        printf("String accepted\n");
        return 0;
    }
}
