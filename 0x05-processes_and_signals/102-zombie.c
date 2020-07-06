#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - creates 5 zombie processes
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates five zombie process
 *
 * Return: 0
 */

int main(void)
{
	short x;
	pid_t child;

	for (x = 0; x < 5; x++)
	{
		child = fork();
		if (!child)
			exit(0);
		printf("Zombie process created, PID: %d\n", getpid());
	}
	infinite_while();
	return (0);
}