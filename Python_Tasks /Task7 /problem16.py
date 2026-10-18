# Problem: Caesar Cipher

# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    
    k = k % 26
    result = []
    
    for char in s:
        if 'a' <= char <= 'z':
        
            shifted = ord('a') + (ord(char) - ord('a') + k) % 26
            result.append(chr(shifted))
        elif 'A' <= char <= 'Z':
          
            shifted = ord('A') + (ord(char) - ord('A') + k) % 26
            result.append(chr(shifted))
        else:
            
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

