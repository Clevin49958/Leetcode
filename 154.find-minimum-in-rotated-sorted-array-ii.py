#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        while nums[0] == nums[-1] and len(nums) > 1:
            nums.pop()
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start + end) // 2
            print(start, end, mid)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            else:
                if nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid
        print(start, end)
        if start == len(nums) - 1 and nums[start] > nums[start - 1]:
            return nums[0]
        return nums[start]
        
# @lc code=end

