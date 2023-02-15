#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        facts = [1] * (n - 1)
        for i in range(1, n - 1):
            facts[i] = (i + 1) * facts[i - 1]
        ans = []
        options = [str(x) for x in range(1, n + 1)]
        k-=1
        for size in reversed(facts):
            ans.append(options.pop(k // size))
            k %= size
        ans.append(options.pop())
        return ''.join(ans)
# @lc code=end
from util import test_local
test_local(
    Solution().getPermutation,
    (3, 3),
    (4, 9),
    (3, 1),
    expand=True
)
