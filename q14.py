from functools import reduce
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def cp(a: str, b: str) -> str:
            l = min(len(a), len(b))
            if l == 0:
                return ""
            idx = 0
            while idx < l and a[idx] == b[idx]:
                idx += 1
            return a[0:idx]
        cm = reduce(cp, strs, strs[0])
        return cm

ins = [
    ["flower","flow","flight"],
    ['bcd', '', 'abc'],
]

sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.longestCommonPrefix(v)
    print(res)