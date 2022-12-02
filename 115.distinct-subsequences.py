#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for c in s:
            for j in range(len(t), 0, -1):
                if c == t[j-1]:
                    dp[j] += dp[j-1]
            pass
        return dp[-1]
# @lc code=end

