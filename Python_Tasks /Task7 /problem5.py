# Problem: Alternating Characters

# HackerRank: https://www.hackerrank.com/challenges/alternating-characters/problem

import os
import sys

def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    # Read the number of queries
    q = int(input().strip())

    for _ in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)

