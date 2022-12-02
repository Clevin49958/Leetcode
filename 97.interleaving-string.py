#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(2)]
        dp[0][0], dp[1][0] = True, True

        ns1, ns2, ns3 = len(s1), len(s2), len(s3)
        if ns1 == 0:
            return s2 == s3
        if ns2 == 0:
            return s1 == s3
        # cache = [False, False]
        for iteration in range(ns3):
            for idx in range(ns2, -1, -1):
                temp = iteration - idx < ns1 and iteration - idx >= 0 and s1[iteration - idx] == s3[iteration] and (dp[1][idx] or dp[0][idx])
                dp[0][idx] = temp
                dp[1][idx] = s2[idx-1] == s3[iteration] and (dp[1][idx-1] or dp[0][idx - 1])
        return dp[1][-1] or dp[0][-1]
# @lc code=end
from util import test_local
test_local(
    Solution().isInterleave,
    ("aabcc", "dbbca", "aadbbcbcac"),
    ("aabcc", "dbbca", "aadbbbaccc"),
    ("", "", ""),
    ("db", "b", "cbb"),
    expand=True,
    # pause=3
)

