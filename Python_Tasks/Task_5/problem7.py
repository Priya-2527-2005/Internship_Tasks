# Problem : Symmetric Difference

# HackerRank : https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int,input().split()))
n = int(input())
b = set(map(int,input().split()))

ans = sorted(a.symmetric_difference(b))

for i in ans:
    print(i)


