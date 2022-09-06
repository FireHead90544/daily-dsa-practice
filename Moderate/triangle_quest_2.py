# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/triangle-quest-2/problem
# Language: Python3
# Difficulty: Moderate

if __name__ == "__main__": # To succeed the channel you need to remove the comments, extra lines and remove the if __name__ == "__main__" part as well
    for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
        print(((10**i - 1)//9)**2) # for i > 1, (10^i)-1 gives us 999... (i times), diving it by 9, gives us 111 (i times), this is what we needed, now just square it and you get your pattern :)