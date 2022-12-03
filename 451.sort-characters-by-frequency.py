#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        for char, count in Counter(s).most_common():
            ans += char * count
        return ans
# @lc code=end

