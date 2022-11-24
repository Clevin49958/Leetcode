#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from collections import Counter, defaultdict
from functools import cache

# destruction approach
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 == s2
        s1_counter, s1_back = Counter(), Counter()
        forward_counter, backward_counter = Counter(), Counter()
        for i in range(len(s1)//2):
            s1_counter[s1[i]] += 1
            s1_back[s1[-i-1]] += 1
            forward_counter[s2[i]] += 1
            backward_counter[s2[-1-i]] += 1
            if s1_counter == forward_counter:
                if self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i+1:], s2[i + 1:]):
                    return True
            if s1_counter == backward_counter:
                if self.isScramble(s1[:i + 1], s2[-1-i:]) and self.isScramble(s1[i + 1:], s2[:-1-i]):
                    return True
            
            if s1_back == forward_counter:
                if self.isScramble(s1[-i-1:], s2[:i + 1]) and self.isScramble(s1[:-i-1], s2[i + 1:]):
                    return True
            if s1_back == backward_counter:
                if self.isScramble(s1[-i-1:], s2[-1-i:]) and self.isScramble(s1[:-i-1], s2[:-1-i]):
                    return True
        return False
        

# @lc code=end

from util import test_local
test_local(
    Solution().isScramble,
    ("great", "rgeat"),
    ("abcde", "caebd"),
    ("abcdef", "dcaebf"),
    ("abc", "abd"),
    ("abacad", "dcbaaa"),
    ("abca","caba"),
    ("abba", "abab"),
    ("abcdbdacbdac","bdacabcdbdac"),
    ("eebaacbcbcadaaedceaaacadccd",
"eadcaacabaddaceacbceaabeccd"),
    expand=True,
    sol=[True, False, False, False, True, True, True, True, False],
    pause=-2
)
# expect