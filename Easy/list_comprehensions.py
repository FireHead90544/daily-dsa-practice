# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Language: Python3
# Difficulty: Easy

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([
        [i, j, k]
        for i in range(x+1) for j in range(y+1) for k in range(z+1) 
        if not sum([i, j, k]) == n
    ]) # Actually a one liner, but just for the sake of clarity used multiple lines :)