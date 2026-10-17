# Problem: Finding the Percentage

# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scores = student_marks[query_name]
    
    average_score = sum(scores)/len(scores)
    print(f"{average_score:.2f}")


