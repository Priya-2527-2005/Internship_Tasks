# Problem: Two Strings

# HackerRank: https://www.hackerrank.com/challenges/two-strings/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

