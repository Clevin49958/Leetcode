#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
from util import test_local

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        def count(s):
            curr = s[0]
            count = 1
            res = []
            for char in s[1:]:
                if char == curr:
                    count += 1
                else:
                    res.extend((str(count), str(curr)))
                    curr = char
                    count = 1
            res.extend((str(count), str(curr)))
            return "".join(res)

        for _ in range(n - 1):
            s = count(s)
            print(s)
        return s


# @lc code=end

test_local(Solution().countAndSay, 2, 3, 4, 5)
