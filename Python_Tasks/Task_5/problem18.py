# Problem: The Minion Game

# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    
    for i in range(length):
        # Every substring starting at index i contributes (length - i) to the score
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
            
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

