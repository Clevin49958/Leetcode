#
# @lc app=leetcode id=2400 lang=python3
#
# [2400] Number of Ways to Reach a Position After Exactly k Steps
#

# @lc code=start
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        width = abs(endPos - startPos)
        half = 500
        n = width + half * 2 + 3
        dp = [0] * n
        mod = 1_000_000_007
        start_idx = half + 1 if startPos <= endPos else half + 1 + width
        dp[start_idx] = 1
        # print(dp)
        for j in range(k):
            dp_old = dp
            dp = [0] * n
            for i in range(1, n - 1):
                dp[i] = (dp_old[i-1] + dp_old[i + 1]) % mod
            # print(dp)
        return dp[n - start_idx - 1] % mod
        


# @lc code=end
print(1_000_000_007)
import util
util.test_local(
    Solution().numberOfWays,
    (2,1,3),
    (5,2,10),
    (989, 1000, 99),
    expand=True
)
