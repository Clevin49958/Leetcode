#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(','[','{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if abs(ord(c) - ord(p)) > 3:
                    return False
        
        return len(stack) == 0
        
# @lc code=end

ins = [
    "()",
    "(){}",
    "({})",
    "({})(",
    "(})"

]

sol = Solution()
for v in ins:
    print('In: ', v)
    res = sol.isValid(v)
    print(res)