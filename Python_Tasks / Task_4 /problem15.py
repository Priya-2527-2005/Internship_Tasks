# Problem: Word Order

# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    """Counter that remembers the order elements are first seen."""
    pass

def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n+1]
    

    word_counts = OrderedCounter(words)
    
    
    print(len(word_counts))
    

    print(*(word_counts.values()))

if __name__ == '__main__':
    main()
