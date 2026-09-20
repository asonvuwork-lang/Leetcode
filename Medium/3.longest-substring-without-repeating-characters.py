#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = []
        long = 0
        for x in range(len(s)):
            while s[x] in letter: 
                letter.pop(0)
            letter.append(s[x])
            long = max(long,len(letter))
        return long

# @lc code=end

