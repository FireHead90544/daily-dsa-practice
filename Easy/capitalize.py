# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/capitalize/problem
# Language: Python3
# Difficulty: Moderate

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join([i.capitalize() for i in s.split(" ")])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()