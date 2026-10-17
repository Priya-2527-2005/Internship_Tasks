# Problem: Piling Up!

# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def solve():
    for _ in range(int(input())):
        n = int(input())
        blocks = deque(map(int, input().split()))
        
        last_block = float('inf')
        possible = True
        
        while blocks:
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop() # Removed .strip()
                
            if current <= last_block:
                last_block = current
            else:
                possible = False
                break
                
        print("Yes" if possible else "No")

if __name__ == "__main__":
    solve()

