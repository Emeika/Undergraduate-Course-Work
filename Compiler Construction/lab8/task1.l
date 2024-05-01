%{
%}

%%
(a|b)
(a|b)$ {printf("Invalid string\n");}
(aa|bb)$ {printf("Valid String\n");}
exit {return 0;}
.	   {printf("%s Invalid character\n", yytext);
        return 1;}
%%

int yywrap(){}
int main()
{
yylex();

return 0;
}
