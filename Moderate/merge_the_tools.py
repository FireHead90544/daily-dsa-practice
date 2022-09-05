# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Language: Python3
# Difficulty: Moderate

import textwrap

def merge_the_tools(string, k):
    splits = textwrap.wrap(string, k)
    final = ["".join([j[1] for j in enumerate(i) if j[1] not in i[:j[0]]]) for i in splits]
    print("\n".join(final))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)