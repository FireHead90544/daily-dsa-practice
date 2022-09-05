# Platform: HackerRank
# Problem: https://www.hackerrank.com/challenges/the-minion-game/problem
# Language: Python3
# Difficulty: Moderate

def minion_game(string):
    players = {"stuart": 0, "kevin": 0}
    for i in range(len(string)):
        score = len(string) - i # length of string from current index to end
        round_winner = "kevin" if string[i] in "AEIOU" else "stuart" # kevin's the winner if the substring contains vowel else stuart's the winner
        players[round_winner] += score # increment the winner's score
        
    print("Draw") if players["kevin"] == players["stuart"] else (print(f"Kevin {players['kevin']}") if players['kevin'] > players['stuart'] else print(f"Stuart {players['stuart']}"))
    

if __name__ == '__main__':
    s = input()
    minion_game(s)