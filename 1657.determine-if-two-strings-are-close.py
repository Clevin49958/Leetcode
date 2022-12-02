#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return Counter(c1.values()) == Counter(c2.values()) and c1.keys() == c2.keys()
# @lc code=end

from util import test_local
test_local(
    Solution().closeStrings,
    ("uau", "ssx"),
    ("uxx", "uss"),
    expand=True
)