# Problem : Set.add()

# HackerRank : https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
country_set = set()

for i in range(n):
    country = input().strip()
    country_set.add(country)
    
print(len(country_set))


