#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
newarr=(arr[len(arr)+1::-1])
print((' '.join(str(e) for e in newarr)))

