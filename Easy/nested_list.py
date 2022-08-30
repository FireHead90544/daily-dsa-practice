# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/nested-list/problem
# Language: Python3
# Difficulty: Easy

if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
        
    s_lowest_score = sorted(set([s[1] for s in data]))[1] # Get all the unique scores, sort them and grab the score at first index (pos. 2)
    bad_peeps = sorted([i[0] for i in data if i[1]==s_lowest_score]) # Peeps with second lowest score
    print("\n".join(bad_peeps))