# Problem: Seperate the Numbers

# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    # If the string starts with '0', it can never be valid
    if s[0] == '0':
        print("NO")
        return

    n = len(s)
    # The first number can at most be half the length of the string
    for i in range(1, n // 2 + 1):
        first_str = s[:i]
        first_num = int(first_str)
        
        # Reconstruct the sequence starting with first_num
        current_num = first_num
        reconstructed = str(current_num)
        
        while len(reconstructed) < n:
            current_num += 1
            reconstructed += str(current_num)
            
        # Check if the reconstructed string matches the input string
        if reconstructed == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        separateNumbers(s)

