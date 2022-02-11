from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda row: row[1])
        index = 0
        last_index = len(sorted_nums) - 1
        sum = sorted_nums[index][1] + sorted_nums[last_index][1]
        while sum != target:
            if sum > target:
                last_index -= 1    
                sum = sorted_nums[index][1] + sorted_nums[last_index][1]
            elif sum < target:
                index += 1
                sum = sorted_nums[index][1] + sorted_nums[last_index][1]
        return [sorted_nums[index][0], sorted_nums[last_index][0]]


