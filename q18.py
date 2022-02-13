
from typing import List

import numpy as np


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []
        nums.sort()
        out = set()
        # print(nums)
        lnums = len(nums)
        i = 0
        while i < len(nums) - 3:
            l = i + 1
            while l < len(nums) - 2:
                j = l + 1
                k = lnums - 1

                def get_sum():
                    nonlocal i, j, k, l
                    return nums[i] + nums[j] + nums[k] + nums[l]

                def update_closest():
                    nonlocal out
                    s = get_sum()
                    return s - target

                while j < k:
                    res = update_closest()
                    if res == 0:
                        out.add((nums[i], nums[l], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif res > 0:
                        k -= 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                    elif res < 0:
                        j += 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                l += 1
                while l < len(nums) - 2 and nums[l] == nums[l-1]:
                    l += 1
            i += 1

            while i < len(nums) - 3 and nums[i] == nums[i-1]:
                i += 1
        return list(map(list, out))


ins = [[1, 0, -1, 0, -2, 2], [2, 2, 2, 2, 2], [-2, -1, -1, 1, 1, 2, 2]
       ]
sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.fourSum(v, 0)
    print(res)
