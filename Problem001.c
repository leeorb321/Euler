/** Problem001.c
  *
  * Project Euler: Problem 1
  * 
  * Problem: Find sum of all natural numbers
  * that are multuples of 3 or 5 below 1000.
  *
  */

#include <stdio.h>

int main(void) {
	// create variable to store sum of multiple of 3, 5
	int multiples_sum = 0;
	
	// loop thru set of numbers to check whether multiples of 3, 5
	for (int i = 0; i < 1000; i++)
	{
	    // add to storage variable if current number meets criteria
	    if ((i % 3 == 0) || (i % 5 == 0)) multiples_sum += i;
	}
	
	// print solution
	printf("The answer is: %i", multiples_sum);
	
	return 0;
}
