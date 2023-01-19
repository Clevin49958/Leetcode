#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def is_palindrome(self, s: str):
        n = len(s)
        return s[:n // 2] == s[-n//2+1:][::-1]
    def partition(self, s: str) -> List[List[str]]:
        def recur(s, idx, arr, ans):
            if idx == len(s):
                ans.append(arr[:])
                return
            for i in range(idx + 1, len(s)):
                if self.is_palindrome(s[idx:i]):
                    arr.append(s[idx:i])
                    recur(s, i, arr, ans)
                    arr.pop()
        ans = []
        recur(s, 0, [], ans)
        return ans
            
# @lc code=end

from util import test_local
test_local(
    Solution().partition,
    "aab"
)