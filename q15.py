from typing import List
import numpy as np


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        v, cnt = np.unique(nums, return_counts=True)
        dict_ = {k: val for (k, val) in zip(v, cnt)}
        out = set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                x = nums[i]
                y = nums[j]
                s = x + y
                local_count = 0
                if x == -s:
                    local_count += 1
                if y == -s:
                    local_count += 1
                if -s in dict_ and dict_[-s] > local_count and -s >= y:
                    # print(x, y, -s)
                    out.add((x, y, -s))
        return list(map(list, out))

ins = [
    [-1,0,1,2,-1,-4],
    [0],
    [],
    [0,0,0],
    [0, -1, 3], 
    [-4, 2, 2, 2],
    [-4, 2, 3]
]


sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.threeSum(v)
    print(res)