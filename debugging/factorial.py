#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Input must be a non-negative integer.")
        else:
            f = factorial(num)
except ValueError:
    print("Please provide a valid integer.")
except IndexError:
    print("Usage: {} <number>".format(sys.argv[0]))