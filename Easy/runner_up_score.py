# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Language: Python3
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    print(sorted([i for i in arr if i < max(arr)])[-1])