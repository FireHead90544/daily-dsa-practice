# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Language: Python3
# Difficulty: Easy

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if sub_string in string[i:i+len(sub_string)]:
            count += 1
    
    return count


# Driver Code
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)