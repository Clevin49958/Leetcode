#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        sum = numbers[start] + numbers[end]
        while sum != target:
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            
            sum = numbers[start] + numbers[end]
        return [start + 1, end + 1]
# @lc code=end

