#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = ""
        num2 = ""

        for x in range(len(l1),0,-1):
            num1 += l1[x]
        for x in range(len(l2),0,-1):
            num2 += l2[x]

        result = int(num1) + int(num2)
        result = str(result)[::-1]

        resultList = ListNode()
        for x in range(1,len(result)):
            resultList.val(result[x])
            resultList.next()

        return resultList


            
# @lc code=end

