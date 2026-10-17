# Problem: Nested Lists

# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    # Extract unique scores and sort them in ascending order
    grades = sorted(list(set(score for name, score in records)))
    
    # Find the second lowest grade
    second_lowest = grades[1]
    
    # Find all students with the second lowest grade and sort their names alphabetically
    second_lowest_students = sorted([name for name, score in records if score == second_lowest])
    
    # Print each student's name on a new line
    for name in second_lowest_students:
        print(name)
