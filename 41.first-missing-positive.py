#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from util import test_local
# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # state: 
        # -1: number present
        # -2: missing
        # >=0: unprocessed
        n = len(nums)
        nums.append(0)
        # chop off irrelevant values
        for i in range(n):
            if nums[i] < 0 or nums[i] > n: 
                nums[i] = 0
        
        for i in range(n + 1):
            curr = nums[i]
            while curr >= 0:
                nums[i] = -2
                next = nums[curr]
                nums[curr] = -1
                curr = next
                pass
        for i in range(1, n + 1):
            if nums[i] != -1:
                return i
        return n + 1





        
# @lc code=end

test_local(Solution().firstMissingPositive, [1,2,0],[3,4,-1,1], [7,8,9,11,12])