# Platform: LeetCode
# Problem: https://leetcode.com/problems/two-sum/
# Language: Python3
# Difficulty: Easy

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
