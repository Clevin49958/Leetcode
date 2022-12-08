#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # build left
        left = []
        for i in range(k + 1):
            old_i = i
            while left and left[-1][-1] >= nums[i]:
                old_i, _v = left.pop()
            left.append([old_i, nums[i]])
        right = []
        for i in range(len(nums)-1, k-1, -1):
            old_i = i
            while right and right[-1][-1] >= nums[i]:
                old_i, _v = right.pop()
            right.append([old_i, nums[i]])

        max_score = 0
        while len(left) > 1 or len(right) > 1:
            score = min(left[-1][-1], right[-1][-1]) * (right[-1][0]-left[-1][0] + 1)
            if score > max_score:
                max_score = score
            
            next_left = left[-2][-1] if len(left)>1 else 0
            next_right = right[-2][-1] if len(right) > 1 else 0
            if next_left > next_right:
                left.pop()
            else:
                right.pop()

        score = min(left[-1][-1], right[-1][-1]) * (right[-1][0]-left[-1][0] + 1)
        if score > max_score:
            max_score = score
        return max_score

        
# @lc code=end

import util
util.test_local(
    Solution().maximumScore,
    ([1,4,3,7,4,5], 3),
    ([5,5,4,5,4,1,1,1], 0),
    ([1,8,1], 1),
    ([6569,9667,3148,7698,1622,2194,793,9041,1670,1872], 5),
    expand=True
    # ,pause=3
)