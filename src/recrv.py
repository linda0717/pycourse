#!/usr/bin/env python

def fib(n):
    """
    An recursive algorithm for Fibonacci numbers
    """
    if n <= 1: # base case
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib_II(n):
    """
    An iterative algorithm for Fibonacci numbers
    """
    if n == 0:
        return n
    else:
        a = 0
        b = 1
        for i in xrange(n-1):
            c = a + b
            a = b
            b = c
        return c

if __name__ == '__main__':
    result = fib_II(6)
    print result

