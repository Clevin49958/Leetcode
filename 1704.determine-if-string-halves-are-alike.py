#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
from collections import Counter


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        def get_counter(s):
            s = filter(lambda c: c in vowels, s)
            return len([*s])
        c1 = get_counter(s[:n])
        c2 = get_counter(s[n:])
        return c1 == c2

# @lc code=end

from util import test_local
test_local(
    Solution().halvesAreAlike,
    "AbCdEfGh"
)