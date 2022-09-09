# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/word-order/problem
# Language: Python3
# Difficulty: Moderate

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == "__main__":
    n = int(input())
    words = [input().replace("\n", "") for _ in range(n)]
    print(len(set(words))) # Unique occurences
    print(" ".join(str(i) for i in Counter(words).values())) # Count of each word