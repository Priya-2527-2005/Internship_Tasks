# Problem: Alphabet Rangoli

# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        # Get the slice of letters for the current row
        current_chars = alpha[i:size]
        # Reverse them, join with hyphens, then add the reversed slice (excluding the first letter to avoid duplication)
        row = "-".join(current_chars[::-1] + current_chars[1:])
        # Center the row with hyphens to fit the full width (width = 4 * size - 3)
        lines.append(row.center(4 * size - 3, "-"))
        
    # Combine top half, center, and bottom half reversed
    output = lines[::-1] + lines[1:]
    print("\n".join(output))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

