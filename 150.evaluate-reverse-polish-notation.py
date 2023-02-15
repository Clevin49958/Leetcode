#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)

                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                
                case "*":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)

                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                
                case _:
                    stack.append(int(token))
            # print(token, stack)
        return stack[0]

        
# @lc code=end

import util
util.test_local(
    Solution().evalRPN,
    ["2","1","+","3","*"],
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
)