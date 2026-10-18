# Problem: Super Reduced String

# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def superReducedString(s):
    stack = []
    for char in s:
        
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    
    result = "".join(stack)
    return result if result else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

