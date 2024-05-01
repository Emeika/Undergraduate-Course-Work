%%
exit                                     {return 0;}
[0 - 9]{5}[- ][0 - 9]{7}[- ][0 - 9]      {printf("Valid ID. Number is: %s\n", yytext);}
[^\n]+                              {printf("Invalid ID. Number is: %s\n", yytext);}
%%

int yywrap(){}
int main()
{
yylex();

return 0;
}