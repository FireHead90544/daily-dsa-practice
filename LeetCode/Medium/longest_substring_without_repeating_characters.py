# Platform: LeetCode
# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Language: Python3
# Difficulty: Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            subs = ""
            for j in range(i, len(s)):
                if s[j] not in subs:
                    subs += s[j]
                    max_len = max(max_len, len(subs))
                else:
                    break

        return max_len
