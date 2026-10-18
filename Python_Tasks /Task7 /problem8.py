# Problem: Gemstones

# HackerRank: https://www.hackerrank.com/challenges/gem-stones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.

def gemstones(arr):
    # Convert each string to a set of its characters, 
    # then find the intersection across all sets to get common minerals.
    common_minerals = set(arr[0])
    for rock in arr[1:]:
        common_minerals.intersection_update(rock)
        
    return len(common_minerals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

