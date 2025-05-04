#include <stdio.h>
#include <string.h>
void vuln_func(char * input_)
{	
	char buffer[256];
	strcpy(buffer,input);
	}
	
