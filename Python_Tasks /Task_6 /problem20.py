# Problem: Validating phone numbers

# HackerRank: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    # A valid mobile number is a 10-digit number starting with 7, 8, or 9.
    pattern = re.compile(r"^[789]\d{9}$")
    
    for i in range(1, n + 1):
        if i < len(input_data):
            number = input_data[i].strip()
            if pattern.match(number):
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    solve()

