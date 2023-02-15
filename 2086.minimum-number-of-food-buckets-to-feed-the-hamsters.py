#
# @lc app=leetcode id=2086 lang=python3
#
# [2086] Minimum Number of Food Buckets to Feed the Hamsters
#

# @lc code=start
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamesters = list(hamsters)
        n = len(hamesters)
        foods = 0
        for i, spot in enumerate(hamesters):
            if spot == 'H' and not ((i >= 1 and hamesters[i - 1] == 'f') or (i <= n - 2 and hamesters[i + 1] == 'f')):
                if i <= n - 2 and hamesters[i + 1] == '.':
                    hamesters[i + 1] = 'f'
                elif i >= 1 and hamesters[i - 1] == '.':
                    hamesters[i - 1] = 'f'
                else:
                    return -1
                foods += 1
        return foods
# @lc code=end

