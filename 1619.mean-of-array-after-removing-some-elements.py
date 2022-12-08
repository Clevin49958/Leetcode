#
# @lc app=leetcode id=1619 lang=python3
#
# [1619] Mean of Array After Removing Some Elements
#

# @lc code=start
from heapq import heappush, heappushpop
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        percentage = len(arr) //20
        arr.sort()
        return sum(arr[percentage:-percentage]) / (len(arr) - percentage * 2)

    # def oldTrimMean(self, arr:List[int]):
    #     percentage = len(arr) //20
    #     min_heap = []
    #     max_heap = []
    #     total = sum(arr)
    #     def fixed_push(heap, item):
    #         if len(heap) < percentage:
    #             heappush(heap, item)
    #         else:
    #             heappushpop(heap, item)
    #     for val in arr:
    #         fixed_push(min_heap, -val)
    #         fixed_push(max_heap, val)
    #     return ((total + sum(min_heap) - sum(max_heap)) / (len(arr) - percentage * 2))

# @lc code=end

