# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/string-validators/problem
# Language: Python3
# Difficulty: Easy

if __name__ == '__main__':
    s = input()
    print(True) if any(i.isalnum() for i in s) else print(False)
    print(True) if any(i.isalpha() for i in s) else print(False)
    print(True) if any(i.isdigit() for i in s) else print(False)
    print(True) if any(i.islower() for i in s) else print(False)
    print(True) if any(i.isupper() for i in s) else print(False)