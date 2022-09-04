# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Language: Python3
# Difficulty: Easy

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    N, M = map(int, input().split(" ")) # Top to center
    for i in range(1, (N//2)+1):
        print(str(".|."*(i+(i-1))).center(M, '-'))
    print("WELCOME".center(M, '-')) # Center 'WELCOME' part
    for i in range(N//2, 0, -1): # Center to bottom
        print(str(".|."*(i+(i-1))).center(M, '-'))