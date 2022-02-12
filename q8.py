class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        output = 0
        is_still_leading_space = True
        idx = 0
        if len(s) == 0:
            return 0
        while is_still_leading_space and idx < len(s):
            if s[idx] != " ":
                is_still_leading_space = False
                break
            idx += 1
        if idx < len(s):
            if s[idx] == "+":
                idx += 1
            elif s[idx] == '-':
                idx += 1
                sign = -1
        
        threshold = 2 ** 31
        if sign == 1:
            threshold -= 1
        while idx < len(s) and s[idx] >= '0' and s[idx] <= '9':
            output *= 10
            output += int(s[idx])
            idx += 1
        
        if output > threshold:
            output = threshold
        return sign * output

s = '  '
sol = Solution()
res = sol.myAtoi(s)
print(res)
