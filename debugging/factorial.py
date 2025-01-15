#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

if len(sys.argv) != 2:
    print("Usage: {} <number>".format(sys.argv[0]))
    sys.exit(1)

try:
    number = int(sys.argv[1])
    f = factorial(number)
    print(f)
except ValueError as e:
    print(e)
    sys.exit(1)
