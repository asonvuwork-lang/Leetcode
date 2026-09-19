#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = int(str(x)[::-1])
        if x == reversed_num:
            return True
        return False

        
# @lc code=end

