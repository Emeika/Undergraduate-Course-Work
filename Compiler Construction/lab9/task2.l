%{
    // declaration section
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    static int ctr = 0;
    static int word = 1;
    char *buff;
    void strange_foo(char *);
%}

%%
    // regex section
[a-zA-Z]+   {strange_foo(yytext);}
\n          {word++;}
[ \t]+      ;
.           ;
%%

int main(int argc, char *argv[])
{
    if (argc!= 3)
    {
        printf("Invalid arguments\n");
        exit(0);
    }

    buff = (char *)malloc(sizeof(char) * 10);
    memset(buff, '\0', 10);
    int i = 0;

    while (argv[2][i] != '\0')
    {
        *(buff + i) = argv[2][i];
        i++;
    }

    FILE *fpin;
    fpin = fopen(argv[1], "r");

    if (fpin)
    {
        yyin = fpin;
    }

    yylex();
    fclose(fpin);
    return 0;
}

void strange_foo(char *ch)
{
    ctr++;
    int flag = 0;

    if (strncmp(ch, buff, 4) == 0)
    {
        flag = 1;
    }

    if (flag)
    {
        printf("Match found: %s\n", ch);
    }
}
