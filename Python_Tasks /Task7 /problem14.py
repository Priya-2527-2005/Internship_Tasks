# Problem: Anagram

# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    count1 = Counter(s1)
    count2 = Counter(s2)
    common_chars = count1 & count2
    changes = sum((count1 - common_chars).values())
    
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s = input()
        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

