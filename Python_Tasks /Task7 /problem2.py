# Problem: The Captain's Room


# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT


k = int(input())
room_list = list(map(int, input().split()))
s1 = set(room_list)
s2 = set()

for room in room_list:
    s2.add(room)

captains_room = (sum(s1) * k - sum(room_list)) // (k - 1)

print(captains_room)
