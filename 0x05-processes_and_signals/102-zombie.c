#include <signal.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>


/**
 * main - an entry point to an example for zombie processes.
 *
 * Return: 0 on succed, 1 on failure.
 **/
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			return (0);
		}
	}

	while (1)
		sleep(1);

	return (0);
}
