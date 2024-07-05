//Write a program to find the number of pipes that can
//simultaneously exist
#include<stdio.h>
int main()
{
	int pipefd[2];//length is always 2
	int count=0;
	while(pipe(pipefd)>=0)
	{
		count++;
	}
	printf("number of pipe will be %d",count);
	return 0;
}
