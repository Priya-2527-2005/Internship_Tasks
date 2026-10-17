# Problem: Set Mutations

# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem


num_elements = int(input())
A = set(map(int, input().split()))
num_operations = int(input())
for i in range(num_operations):
    op_name, _ = input().split()

    other_set = set(map(int, input().split()))
    
    
    if op_name == "update":
        A.update(other_set)
    elif op_name == "intersection_update":
        A.intersection_update(other_set)
    elif op_name == "difference_update":
        A.difference_update(other_set)
    elif op_name == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)


print(sum(A))

