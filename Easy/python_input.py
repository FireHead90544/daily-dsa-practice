# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/input/problem
# Language: Python3
# Difficulty: Easy

if __name__ == "__main__":
    x, k = map(int, input().split())
    P = eval(input())
    print(True) if P == k else print(False)
