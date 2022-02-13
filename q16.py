from typing import List

import numpy


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = numpy.inf
        nums.sort()
        print(nums)
        l = len(nums)
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = l - 1
            def get_sum():
                nonlocal i, j, k
                return nums[i] + nums[j] + nums[k]
            def update_closest():
                nonlocal closest
                s = get_sum()
                if abs(s - target) < abs(closest - target):
                    closest = s
                return s - target
            
            while j < k:
                res = update_closest()
                if res == 0:
                    return get_sum()
                elif res > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif res < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            i += 1
        return closest

ins = [
    [-1,0,1,2,-1,-4],
    [0,0,0],
    [0, -1, 3], 
    [-4, 2, 2, 2],
    [-4, 2, 3],
    [-1,2,1,-4]
]


sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.threeSumClosest(v, 1)
    print(res)
                
            

