# Platform: LeetCode
# Problem: https://leetcode.com/problems/add-two-numbers/
# Language: Python3
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = [[], []]
        while l1:
            n1[0].append(l1.val)
            l1 = l1.next
        while l2:
            n1[1].append(l2.val)
            l2 = l2.next
        s = [
                int(i) for i in str(
                    int("".join([str(i) for i in n1[0][::-1]])) + int("".join([str(i) for i in n1[1][::-1]]))
                )[::-1]
            ]
        res = ListNode(s[0])
        current = res

        for i in range(1, len(s)):
            current.next = ListNode(s[i])
            current = current.next
        return res
