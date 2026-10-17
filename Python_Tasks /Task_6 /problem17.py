# Problem:Check Strict Superset


# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem


A = set(input().split())
n = int(input())

is_strict_superset = True

for _ in range(n):
    other_set = set(input().split())
    # A strict superset must strictly contain the other set 
    # (i.e., A must contain all elements of other_set, and A must be larger)
    if not (A.issuperset(other_set) and len(A) > len(other_set)):
        is_strict_superset = False
        break

print(is_strict_superset)

