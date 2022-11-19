#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

import math
from typing import List
# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # return the max single element if they are all negative
        for v in nums:
            if v >= 0:
                break
        else:
            return max(nums)

        start = 0
        end = 0
        maxs = -math.inf
            
        s = 0
        temp = 0
        # move end
        endi = end
        while endi < len(nums):
            temp += nums[endi]
            if temp >= 0:
                end = endi
                s += temp
                maxs = max(maxs, s)
                temp = 0
            elif s + temp < 0:
                start = endi + 1
                end = start
                temp = 0
                s = 0
                
            endi += 1
        return maxs

# @lc code=end
from util import test_local
test_local(Solution().maxSubArray,  [-2,1,-3,4,-1,2,1,-5,4], [-2,1,-3,4,-1,2,1,-5,4, -100, 20], [1], [-2])
