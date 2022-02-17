#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        ln, lh = len(needle), len(haystack)
        for i in range(lh - ln + 1):
            print(i, i + ln)
            if haystack[i:i + ln] == needle:
                return i
        return -1

             
# @lc code=end
ins = [
    ("hello", "ll"),
    ("aaaaa", "bba"),
    ("", ""),
    ("abc", "c"),
    ("mississippi", "issip"),
    ("a", "a")
]


sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.strStr(*v)
    print(res)
