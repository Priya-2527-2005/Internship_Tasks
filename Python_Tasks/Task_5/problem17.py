# Problem: No Idea!

# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    
    # Array elements
    arr = input_data[2:2 + n]
    
    # Sets A and B (using sets for O(1) lookups)
    set_a = set(input_data[2 + n : 2 + n + m])
    set_b = set(input_data[2 + n + m:])
    
    # Calculate happiness
    happiness = 0
    for x in arr:
        if x in set_a:
            happiness += 1
        elif x in set_b:
            happiness -= 1
            
    print(happiness)

if __name__ == '__main__':
    solve()


