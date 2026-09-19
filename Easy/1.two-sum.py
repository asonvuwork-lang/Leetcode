#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for i in range(x+1,len(nums)):
                if nums[x] + nums[i] == target:
                    return [x,i]
# @lc code=end

