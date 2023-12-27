# Platform: LeetCode
# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Language: Python3
# Difficulty: Hard

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mgd = sorted(nums1 + nums2)
        l = len(mgd)
        return (mgd[l//2] + mgd[(l//2) - 1])/2 if l%2==0 else mgd[(l-1)//2]