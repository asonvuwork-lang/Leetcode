#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = min(strs)
        last = max(strs)

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return first[:i]

        return first
# @lc code=end

