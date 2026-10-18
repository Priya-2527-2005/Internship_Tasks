# Problem: Sherlock and the Valid String

# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

from collections import Counter
import os
import sys

def isValid(s):
    # Count the frequency of each character
    freq = Counter(s)
    
    # Count the frequencies of those frequencies
    freq_counts = Counter(freq.values())
    
    # Case 1: All characters have the same frequency
    if len(freq_counts) == 1:
        return "YES"
    
    # Case 2: There are more than 2 different frequency values, so it's invalid
    if len(freq_counts) > 2:
        return "NO"
    
    # Case 3: Exactly two different frequency values exist
    f1, count1 = list(freq_counts.items())[0]
    f2, count2 = list(freq_counts.items())[1]
    
    # Sub-case A: One character appears only 1 time, and we can remove it entirely
    if (f1 == 1 and count1 == 1) or (f2 == 1 and count2 == 1):
        return "YES"
    
    # Sub-case B: The difference between the two frequencies is 1, 
    # and the higher frequency occurs only 1 time (so we can remove one instance)
    if (abs(f1 - f2) == 1) and ((f1 > f2 and count1 == 1) or (f2 > f1 and count2 == 1)):
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

