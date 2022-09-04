# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Language: Python3
# Difficulty: Easy

def print_formatted(number):
    pad = len(str(bin(number).replace("0b", "")))
    for i in range(1, number+1):
        print(
            str(i).rjust(pad), 
            str(oct(i)).replace("0o", "").rjust(pad),
            str(hex(i)).replace("0x", "").upper().rjust(pad),
            str(bin(i)).replace("0b", "").rjust(pad)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)