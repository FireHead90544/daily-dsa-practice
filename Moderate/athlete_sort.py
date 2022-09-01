# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem
# Language: Python3
# Difficulty: Moderate

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(N)]
    K = int(input())
    data = sorted(data, key=lambda i: i[K])
    for i in data:
        print(" ".join(str(l) for l in i))