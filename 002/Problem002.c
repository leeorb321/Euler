/** Problem002.c
  *
  * Project Euler: Problem 2
  * 
  * Problem: Find the sum of the even-valued terms in the 
  *          Fibonacci sequence whose value is under 4 million.
  *
  */

#include <stdio.h>

int main(void)
{
    int sum = 0, temp, first = 0, second = 1, limit = 4000000;
    while (second < limit)
    {
        temp = second;
        second += first;
        first = temp;
        if (second % 2 == 0)
            sum += second;
    }
 
    printf("%i\n", sum);
}
