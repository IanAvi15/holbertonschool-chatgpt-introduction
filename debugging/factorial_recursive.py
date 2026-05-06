#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a given number recursively.

    Parameters:
        n (int): The non-negative integer to compute the factorial of.
                 Returns 1 when n is 0 (base case).

    Returns:
        int: The factorial of n, computed as n * (n-1) * ... * 1.
             Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)