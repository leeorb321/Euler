/** Problem007.c
  *
  * Project Euler: Problem 7
  * 
  * Problem: Find the 10,001st prime number.
  *          
  *
  */

#include <stdio.h>
#include <math.h>

#include <time.h>

int is_prime(int num)
{
	if (num == 2)
		return 1;
	if (num < 2 || num % 2 == 0)
		return 0;
	int max_check = (int)(sqrt(num));
	if (max_check % 2 == 0)
		max_check -= 1;
	for (int i = max_check; i > 1; i -= 2)
		if (num % i == 0)
			return 0;
	return 1;
}

int main(void)
{
	clock_t t = clock();

	int num = 10001;
	int current = 2, counter = 0;
	while (counter < num)
	{
		if (is_prime(current) == 1)
			counter++;
		current++;
	}
	printf("%d\n\n", current - 1);

	t = clock() - t;
	double time_taken = ((double)t)/CLOCKS_PER_SEC;
	printf("--- %f seconds ---\n", time_taken);

	return 0;
}