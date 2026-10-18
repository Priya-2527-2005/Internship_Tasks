# Problem: Funny String

# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

import sys

def funnyString(s):
    n = len(s)
    for i in range(n - 1):
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(s[n-1-(i+1)]) - ord(s[n-1-i])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        q = int(input_data[0])
        for i in range(1, q + 1):
            print(funnyString(input_data[i]))

