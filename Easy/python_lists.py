# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/python-lists/problem
# Language: Python3
# Difficulty: Easy

if __name__ == '__main__':
    N = int(input())
    list = []
    cmds = [input().split() for i in range(N)]
    for cmd in cmds:
        if "print" in cmd:
            print(list)
        else:
            eval(f"list.{cmd[0]}({', '.join(cmd[1:])})")