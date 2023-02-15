#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

from functools import cache
# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        # @cache
        # def tree(n):
        #     if n <= 2:
        #         return n
        #     ans = 2 * tree(n-1)
        #     for i in range(1, n-1):
        #         ans += tree(i) * tree(n-i-1)
        #     return ans
        # return tree(n)
        return [1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190][n-1]
# @lc code=end

s = Solution()
print([*map(s.numTrees, range(1, 20))])