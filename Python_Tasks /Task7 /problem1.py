# problem: Set .symmetric_difference() Operation

# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


# Read inputs
n = int(input())
set_a = set(map(int, input().split()))

m = int(input())
set_b = set(map(int, input().split()))

# Find the symmetric difference and print its length
result = set_a.symmetric_difference(set_b)
print(len(result))

