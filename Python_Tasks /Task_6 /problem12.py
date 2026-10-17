# Problem: Set .discard(), .remove() & .pop()

# HackerRank: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    parts = input().split()
    try:
        if parts[0] == 'pop':
            s.pop()
        elif parts[0] == 'remove':
            s.remove(int(parts[1]))
        elif parts[0] == 'discard':
            s.discard(int(parts[1]))
    except KeyError:
        pass

print(sum(s))

