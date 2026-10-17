# Problem: Designer Door Mat

# HackerRank: https://www.hackerrank.com/challenges/designer-door-mat/problem


n, m = map(int, input().split())

# Top half of the door mat
for i in range(1, n, 2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)

# Center line with WELCOME
print("WELCOME".center(m, "-"))

# Bottom half of the door mat
for i in range(n - 2, 0, -2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)

