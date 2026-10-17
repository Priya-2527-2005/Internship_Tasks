# Problem: Collections.Counter()

# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Read the number of shoes
num_shoes = int(input())

# Read the list of shoe sizes and count them using Counter
shoe_sizes = list(map(int, input().split()))
shoe_count = Counter(shoe_sizes)

# Read the number of customers
num_customers = int(input())

total_earned = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    # Check if the shoe size is available in stock
    if shoe_count[size] > 0:
        total_earned += price
        shoe_count[size] -= 1  # Reduce the count of that shoe size

# Print the total money earned
print(total_earned)
