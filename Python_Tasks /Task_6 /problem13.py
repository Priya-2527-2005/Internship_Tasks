# Problem:Set .union() Operation


# HackerRank: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english_subscribers = set(map(int, input().split()))

b = int(input())
french_subscribers = set(map(int, input().split()))

# Find the union of both sets to get all students with at least one subscription
total_subscribers = english_subscribers.union(french_subscribers)

# Print the total count
print(len(total_subscribers))

