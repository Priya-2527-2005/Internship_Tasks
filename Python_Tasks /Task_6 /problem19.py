# Problem: Company Logo

# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # Count the frequency of each character
    counts = Counter(s)
    

    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 characters and their counts
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")

