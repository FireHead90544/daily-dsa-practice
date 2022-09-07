# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
# Language: Python3
# Difficulty: Moderate

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    f = "%a %d %b %Y %H:%M:%S %z"
    diff = (datetime.datetime.strptime(t1, f) - datetime.datetime.strptime(t2, f)).total_seconds()
    return f"{round(abs(diff))}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()