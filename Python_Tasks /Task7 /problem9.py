# Problem: Beautiful Binary String

# HackerRank: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    
    changes = 0
    i = 0
    b_list = list(b)
    while i < len(b_list) - 2:
        if b_list[i] == '0' and b_list[i+1] == '1' and b_list[i+2] == '0':
            changes += 1
            # Skip ahead by 3 because we fix the pattern at index i+2
            i += 3
        else:
            i += 1
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

