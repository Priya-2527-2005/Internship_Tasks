# Problem: Check Subset


# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    a_size = int(input())
    set_a = set(map(int, input().split()))
    b_size = int(input())
    set_b = set(map(int, input().split()))
    
    # Use the issubset() method to check if set_a is a subset of set_b
    print(set_a.issubset(set_b))

