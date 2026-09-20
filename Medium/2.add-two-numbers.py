#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = ""
        num2 = ""

        while l1!= None:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            num2 += str(l2.val)
            l2 = l2.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        result = int(num1) + int(num2)
        result = str(result)[::-1]
        LR = ListNode()
        current = LR
        for x in range(len(result)):
            current.next = ListNode(int(result[x]))
            current = current.next

        return LR.next
# @lc code=end

