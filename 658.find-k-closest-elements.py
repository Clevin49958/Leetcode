#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def get_distance(i: int):
            v = arr[i]
            return abs(v - x) +( 0.5 if v > x else 0)

        start = 0
        end = len(arr) - k
        while start + 1 <= end:
            mid = (start + end) // 2
            dist_mid = get_distance(mid)
            dist_next = get_distance(mid + k)
            print(start, end, mid, dist_mid, dist_next)
            if dist_mid < dist_next:
                if end == mid:
                    break
                end = mid
            elif dist_mid > dist_next:
                start = mid + 1
            else:
                # dist eq => mid == next
                assert arr[mid] == arr[mid + k]
                if x > arr[mid]:
                    start = mid + 1
                elif x < arr[mid]:
                    end = mid - 1
                else:
                    break
        return [arr[i] for i in range(start, start + k)]
            

        
# @lc code=end

ins = [
    ([1,2,3,4,5,6,8,9,10,11,12,13], 3, 13)
]
sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.findClosestElements(*v)
    print(res)
