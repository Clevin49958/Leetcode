#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        s = list(palindrome)
        for i in range(len(s)):
            if s[i] != "a":
                s[i] = "a"
                break
        else:
            s[i] = "b"
        return "".join(s)


# @lc code=end
