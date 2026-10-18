# Problem: Game of Thrones - 1

# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

from collections import Counter
import os
import sys

def gameOfThrones(s):
    
    char_counts = Counter(s)
    

    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
   
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

