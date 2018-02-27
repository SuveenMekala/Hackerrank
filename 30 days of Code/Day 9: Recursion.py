#!/bin/python3

import sys

def factorial(n):
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    return(prod)
if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)

