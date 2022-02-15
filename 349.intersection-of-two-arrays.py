#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i1 = 0
        i2 = 0
        res = set()
        nums1.sort()
        nums2.sort()
        def incre_i1():
            nonlocal i1
            if i1 < len(nums1) - 1:
                i1 += 1
                return True
            return False
        def incre_i2():
            nonlocal i2
            if i2 < len(nums2) - 1:
                i2 += 1
                return True
            return False
        print(nums1, nums2)
        while i1 < len(nums1) and i2 < len(nums2):
            print(i1, i2, nums1[i1], nums2[i2])
            if nums1[i1] == nums2[i2]:
                res.add(nums1[i1])
            if i1 == len(nums1) -1 and i2 == len(nums2) - 1:
                break
            if nums1[i1] == nums2[i2]:
                incre_i1()
                incre_i2()
            elif nums1[i1] < nums2[i2]:
                if not incre_i1():
                    incre_i2()
            else:
                if not incre_i2():
                    incre_i1()
        return list(res)

        
# @lc code=end

Solution().intersection([1,2,3],[1])
