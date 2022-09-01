# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/any-or-all/problem
# Language: Python3
# Difficulty: Easy

if __name__ == '__main__':
    N = int(input())
    ints = list(map(int, input().split()))
    print(True) if (all([True if i > 0 else False for i in ints]) and any([i==int(str(i)[::-1]) if i>0 else i==-int(str(i)[::-1][0:-1]) for i in ints])) else print(False) # There was an additional challenge to try to complete the program in less than 3 lines, so I did (don't mind the if __name__ == "__main__" and comments one), and btw there is no need to check for negative palindrome integers since negative integers are meant to be discarded in the previous condition but still I added it because why not :)