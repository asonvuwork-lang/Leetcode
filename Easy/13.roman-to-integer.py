#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IX':9,
            'IV':4,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }
        total = 0
        x = 0
        while x < len(s):
            if x + 1 < len(s) and s[x:x+2] in symbol:
                total += symbol[s[x:x+2]]
                x += 2
            else:
                total += symbol[s[x]]
                x += 1
        return total
# @lc code=end

