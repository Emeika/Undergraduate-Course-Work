%{
    // declaration section
%}

%%
    // regex section
.   {fprintf(yyout, "%s", yytext);}
%%

int main()
{
    extern FILE *yyin, *yyout;
    yyin = fopen("input.txt", "r");
    yylex();
    printf("\n");
    return 0;
}
