from turtle import st
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getA(start, end):
            return min(height[start], height[end]) * (end - start)
        start = 0
        end = len(height) - 1
        
        def getMaxArea(start: int, end: int) -> int:
            # print(start, end)
            a = getA(start, end)
            lower = min(height[end], height[start])
            idx = end if height[start] > height[end] else start
            for i in range(start + 1, end) if idx == start else range(end - 1, start, -1):
                if height[i] > lower:
                    if idx == start:
                        b = getMaxArea(i, end)
                    else:
                        b = getMaxArea(start, i)
                    if b > a:
                        a = b
                    break
            return a
        return getMaxArea(start, end)

ss = [
    # [1, 1],
    [1,8,6,2,5,4,8,3,7],
    [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191],
    [10,9,8,7,6,5,4,3,2,1]
]
for s in ss:
    sol = Solution()
    res = sol.maxArea(s)
    print(s, res, sep='\n')
