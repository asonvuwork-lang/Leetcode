#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combine = nums1 + nums2
        combine = sorted(combine)

        n = len(combine)
        middle = n // 2

        if n % 2 == 1:
            return combine[middle]
        else:
            return (combine[middle - 1] + combine[middle]) / 2
# @lc code=end

