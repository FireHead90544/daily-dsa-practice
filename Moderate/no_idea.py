# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Language: Python3
# Difficulty: Moderate

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    print(sum([1 for i in arr if i in A]) - sum([1 for i in arr if i in B]))