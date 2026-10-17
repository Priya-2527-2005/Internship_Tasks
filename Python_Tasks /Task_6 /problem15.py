# Problem: Set .difference() Operation


# HackerRank: https://www.hackerrank.com/challenges/py-set-difference-operation/problem


# Read the number of English newspaper subscribers (not strictly needed for sets, but part of the input)
n_english = int(input())
# Read the English subscriber roll numbers into a set
english_set = set(map(int, input().split()))

# Read the number of French newspaper subscribers
n_french = int(input())
# Read the French subscriber roll numbers into a set
french_set = set(map(int, input().split()))

# Find students subscribed to only English newspapers using the .difference() method
only_english = english_set.difference(french_set)

# Print the total count
print(len(only_english))


